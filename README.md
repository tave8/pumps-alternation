# Algoritmo di soglie con isteresi

Questo è un algoritmo che, in base a un livello raggiunto, a delle soglie e al numero di pompe attive, ti dice se attivare o disattivare una pompa in ogni dato momento. 

- [Vedi grafici](#grafici)
- [Vai alla simulazione](/src/simulation.py)
- [Vai all'algoritmo](/src/lib/algo.py) 
- [Come funziona la simulazione / modello di esecuzione PLC](#come-funziona-la-simulazione)
- [Come ho ragionato: Vai a unit test](/tests/test_decidi_se_attivare_o_disattivare_pompe.py)

✅ Cosa promette: Un sistema più mantenibile, comprensibile e modularizzato grazie alla separazione della logica di decisione da quella di implementazione.
   La modifica delle soglie, e quindi la configurazione, è una banalità. Non si deve ritoccare il codice sorgente. 
   La decisione di attivazione / disattivazione pompa è una semplice chiamata di funzione.  

❌ Cosa non promette: Un'implementazione pronta all'uso. L'alternanza delle pompe con logiche di implementazione personalizzate. (Anche se viene comunque fornita una simulazione)

Cosa include il pacchetto:

- L'algoritmo vero e proprio. Questa è la logica pura, indipendente dagli altri componenti elencati.

- Un'implementazione che permette di simularne il funzionamento, basata su macchina a stati, variazione casuale del livello d'acqua 
  e una "memoria virtuale" che imita la memoria di un PLC (la memoria che sopravvive gli scan cycles). 

- Un report in csv generato ad ogni fine simulazione, per poter analizzare come si comporta l'algoritmo nel tempo. 

Nota: Per semplicità, c'è sola una pompa reale fornita. La complessità verrà aggiunta un po' alla volta quando ha senso.

## Come funziona

Vediamo meglio come funziona.

L'algoritmo non prende la decisione; dice solo se attivare o disattivare una pompa, in ogni dato momento. Prendere la decisione è responsabilità dell'implementazione.

Il tutto è stato pensato con una chiara separazione di responsabilità, modularità, testabilità e leggibilità. I passi dell'algoritmo possono anche essere eseguiti independentemente uno dall'altro.

Re-itero: L'algoritmo ne' conosce ne' gli importa di come verrà implementato, quindi si ha libertà di implementazione. 

Ecco gli input/output:

```
PROCEDURE decidi_se_attivare_o_disattivare_pompe

  INPUT
      livello_attuale: float
      soglie: list
      tot_pompe_attive_adesso: int
  
  OUTPUT
    list[bool, bool]

```


## Come è nata l'idea

L'idea è nata così:

- Tradurlo in PLC. Al momento in cui l'ho scritto, programmarlo subito in PLC mi sembrava un salto troppo grande.
  Ho pensato di creare una versione funzionante, documentata e testata in Python, e solo dopo tradurlo in PLC. 
  Motivo per cui ho mantenuto il codice molto basilare in termini di astrazione (evitando di proposito OOP), 
 proprio perché la facilità di traduzione Python -> PLC è un altro fattore che ho tenuto in considerazione.

- Generalizzare a N soglie. Invece che hardcodare i valori delle soglie. Ricontestualizzare la modifica delle soglie 
  come dati che l'algoritmo riceve in ingresso - senza toccare il codice sorgente. 

- Separare la decisione di attivazione / disattivazione pompe, dalla sua implementazione. Mi interessa sapere solo se attivare / disattivare pompa; 
  Il "come" viene ricontestualizzato come problema di implementazione.


## Grafici

![grafico1](/media/grafico1.png)

![grafico2](/media/grafico2.png)

![grafico3](/media/grafico3.png)

![grafico4](/media/grafico4.png)


## Come avviare la simulazione

Per avviare la simulazione, ti basta eseguire il file [simulation.py](/src/simulation.py).

Si può facilmente regolare la velocità di esecuzione della simulazione (10, 100, ecc. giri al secondo), ma per semplicità, 
ti basta tenerla attiva qualche secondo (anche 4 secondi vanno bene) per avere già centinaia di righe nel csv.


## Come funziona la simulazione

La simulazione si pone un obiettivo, che è quello di simulare un PLC. 

Per fare ciò, servono almeno due meccanismi: un scan cycle e una memoria che sopravvive gli scan cycles.

La simulazione simula la "memoria di un PLC" attraverso un meccanismo furbo ma incredibilmente semplice; Una semplice hashmap passata una sola volta in fase di inizio del loop, e poi ripassata ogni volta ad ogni iterazione. 

Essendo l'hashmap passata per riferimento, questo simula "la memoria che sopravvive gli scan cycles di un PLC", visto che si sta modificando lo stesso oggetto in memoria.

L'intero codice implementativo viene raccolto in una "funzione macchina" da richiamare ad ogni iterazione. 

Questa funzione macchina viene poi passata una funzione che la fa girare nel loop, poi aspetta un po', e poi la ri-esegue, e così via all'infinito fin quando non esci dal programma.

Il codice nella funzione macchina è esattamente il codice che scrivi in PLC! 

Per iniettare logiche custom in modo non-intrusivo, alla fine di ogni iterazione, viene eseguita una callback, che permette di eseguire azioni personalizzate come, ad esempio, fare un dump della "memoria del PLC" ad ogni fine iterazione, generando così un csv.

Ecco il funzionamento in pseudo-codice.

```

machine_func(memoria):

  // In questa funzione metti il codice che vuoi eseguire ad ogni iterazione.
  
  // Posso accedere alla "memoria del PLC"; la memoria persiste, quindi sarà accessibile alla prossima iterazione.
  
  // Un'implementazione con macchina a stati che scriveresti in PLC
  
  case memoria["stato"]:
    
    StatoMacchina.INIZIO:
    
      memoria["stato"] = StatoMacchina.MACCHINA_AVVIATA
    
    StatoMacchina.MACCHINA_AVVIATA
    
      // altra logica
  


// Passo la funzione macchina come argomento di un'altra funzione, che la eseguirà ad ogni iterazione.
// Posso anche inizializzare la memoria del PLC

run_machine_in_loop(machine_func, {
  "stato": StatoMacchina.INIZIO
})

```


## Presupposti

- Soglia N Attivazione > Soglia N Disattivazione (Ogni soglia di attivazione è maggiore della corrispondente soglia di disattivazione)
- Soglia N Attivazione > Soglia N-1 Attivazione (Ogni soglia di attivazione è maggiore della precedente soglia di attivazione)
- Soglia N Disattivazione > Soglia N-1 Disattivazione (Ogni soglia di disattivazione è maggiore della precedente soglia di disattivazione)
