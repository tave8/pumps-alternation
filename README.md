# Algoritmo di Alternanza Pompe basato su Isteresi

Per avviare il programma, vai nel main.py.


Per dimostrare il funzionamento dell'algoritmo, sono forniti i seguenti strumenti:

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
- 