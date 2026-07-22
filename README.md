# Algoritmo di Alternanza Pompe basato su Isteresi

Questo è un algoritmo che, in base a un livello raggiunto, a delle soglie e al numero di pompe attive, ti dice se attivare o disattivare una pompa in ogni dato momento. [Ecco il codice](/src/lib/algo.py) 

[Vedi grafici](#grafici)

L'idea è nata così:

- Tradurlo in PLC. Al momento in cui l'ho scritto, programmarlo subito in PLC mi sembrava un salto troppo grande.
  Ho pensato di creare una versione funzionante, documentata e testata in Python, e solo dopo tradurlo in PLC. 
  Motivo per cui ho mantenuto il codice molto basilare in termini di astrazione (evitando di proposito OOP), 
 proprio perché la facilità di traduzione Python -> PLC è un altro fattore che ho tenuto in considerazione.

- Generalizzare a N soglie. Invece che hardcodare i valori delle soglie. Ricontestualizzare la modifica delle soglie 
  come dati che l'algoritmo riceve in ingresso - senza toccare il codice sorgente. 

- Separare la decisione di attivazione / disattivazione pompe, dalla sua implementazione. Mi interessa sapere solo se attivare / disattivare pompa; 
  Il "come" viene ricontestualizzato come problema di implementazione.


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

Tuttavia, un algoritmo da solo non è molto pratico, serve metterlo alla prova. Infatti ci sono 3 componenti:

- L'algoritmo vero e proprio. Questa è la logica pura, indipendente dagli altri componenti elencati.

- Un'implementazione che permette di simularne il funzionamento, basata su macchina a stati, variazione casuale del livello d'acqua 
  e una "memoria virtuale" che imita la memoria di un PLC (la memoria che sopravvive gli scan cycles). 

- Un report in csv generato ad ogni fine simulazione, per poter analizzare come si comporta l'algoritmo nel tempo. 

Nota: Per semplicità, c'è sola una pompa reale fornita. La complessità verrà aggiunta un po' alla volta quando ha senso.

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

La simulazione simula la "memoria di un PLC" attraverso un meccanismo furbo ma incredibilmente semplice; una semplice hashmap passata
una sola volta in fase di inizio del loop, e poi ripassata ogni volta.

Essendo l'hashmap passata per riferimento, questo simula "la memoria che sopravvive gli scan cycles di un PLC".



- Memoria virtuale. Per simulare il meccanismo di "memoria che sopravvive alle iterazioni", 
  viene passata una singola hashmap che la macchina può modificare. Essendo l'hashmap 
  passata per riferimento dall'esterno, ogni modifica sopravvive alle iterazioni. 

- Csv a fine loop. Il csv contiene il dump delle principali variabili nella memoria virtuale, lette ad ogni fine iterazione.
  Questo permette di analizzare come si comporta il sistema nel tempo.



## Presupposti

- Soglia N Attivazione > Soglia N Disattivazione (Ogni soglia di attivazione è maggiore della corrispondente soglia di disattivazione)
- Soglia N Attivazione > Soglia N-1 Attivazione (Ogni soglia di attivazione è maggiore della precedente soglia di attivazione)
- Soglia N Disattivazione > Soglia N-1 Disattivazione (Ogni soglia di disattivazione è maggiore della precedente soglia di disattivazione)

## Caratteristiche

- Il sistema può attivare o disattivare una sola pompa alla volta per stato. 
- Il sistema esegue un "dump" dei valori che vengono processati ad ogni iterazione



## 

    # Il "seq" sta per "numero sequenza" e rappresenta
    # un numero intero, internamente assegnato, che corrisponde alla soglia.
    # La prima soglia ha numero sequenza 1, la seconda soglia ha numero sequenza 2, ecc.


    # Il numero minimo di pompe attive necessarie è calcolato come
    # la più alta soglia di attivazione raggiunta dal livello attuale (ad esempio il livello dell'acqua)
    # moltiplicato il numero di pompe per ogni soglia.
    # Considera il seguente scenario:
    # - Ad ogni soglia di attivazione raggiunta, scatta 1 pompa
    # - Il livello attuale ha raggiunto la soglia 2
    # - C'è solo 1 pompa attiva
    # La decisione è che va attivata una pompa.