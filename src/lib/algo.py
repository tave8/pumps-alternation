

def decidi_se_attivare_o_disattivare_pompe(livello_attuale: float,
                                           soglie: list[tuple[float, float]],
                                           tot_pompe_attive_adesso: int) -> tuple[bool, bool]:
    """
    Funzione principale. Ritorna le decisioni se attivare o disattivare una sola pompa alla volta.

    Se ci sono più pompe da attivare o disattivare, è responsabilità dell'implementazione
    continuare a richiamare l'algoritmo.

    Tutte le quantità passate devono essere già scalate. Nello specifico,
    livello_attuale e soglie devono essere scalate.

    L'algoritmo assume che livello_attuale e soglie siano scalate (in scala percentuale),
    quindi l'algoritmo NE' scalerà le quantità NE' verificherà che siano scalate. E' tua responsabilità.

    L'ordine in cui vengono passate le soglia conta. Si devono passare le soglie dalla più bassa alla più alta.

    Esempio:

    ```code
        (60, 55)
        (70, 65)
        (80, 75)

    Che rappresenta, concettualmente:

        Soglia attivazione   |    Soglia disattivazione   |   Numero sequenziale (auto-assegnato)
        ------------------------------------------------------------------------------------------
             60                          55                        1
             70                          65                        2
             80                          75                        3
    ```

    In breve, l'implementazione è responsabile / ha la libertà di:
    - Scalare il livello_acqua e le soglie
    - E' libera di interpretare le decisioni di come attivare / disattivare una pompa alla volta
    - Dovrà continuare a chiamare l'algoritmo continuamente

    :param livello_attuale: Il livello attuale dell'acqua.

    :param soglie: una lista di soglia, dove ogni soglia è della forma (soglia attivaz., soglia disattivaz.). L'ordine conta;
        Si parte dalla soglia più bassa a quella più alta.

    :param tot_pompe_attive_adesso: Il numero di pompe attive adesso

    :return: Una tupla di booleani contenente le decisioni se attivare o disattivare una pompa, nello specifico
        (decisione_attiva_pompa, decisione_disattiva_pompa) da usare nel tuo codice implementativo, per decidere
        come implementare questa decisione.
    """

    num_pompe_per_soglia: int = 1

    poche_pompe_attive: bool = ci_sono_poche_pompe_attive(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso,
        num_pompe_per_soglia
    )

    troppe_pompe_attive: bool = ci_sono_troppe_pompe_attive(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso,
        num_pompe_per_soglia
    )

    # Si deve attivare una pompa solo se ci sono poche pompe attive
    decisione_attiva_pompa: bool = poche_pompe_attive
    # Si deve disattivare una pompa solo se ci sono troppo pompe attive
    decisione_disattiva_pompa: bool = troppe_pompe_attive

    return (decisione_attiva_pompa,
            decisione_disattiva_pompa)


def ci_sono_poche_pompe_attive(livello_attuale: float,
                               soglie: list[tuple[float, float]],
                               tot_pompe_attive_adesso: int,
                               num_pompe_per_soglia: int) -> bool:

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_min(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    # Ci sono poche pompe attive in questo istante se le pompe attive adesso
    # sono meno del minimo necessarie
    return tot_pompe_attive_adesso < tot_pompe_attive_necessarie_min


def ci_sono_troppe_pompe_attive(livello_attuale: float,
                               soglie: list[tuple[float, float]],
                               tot_pompe_attive_adesso: int,
                               num_pompe_per_soglia: int) -> bool:

    tot_pompe_attive_necessarie_max = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    # Ci sono troppo pompe attive in questo istante se il numero di pompe attive adesso
    # è maggiore del massimo necessario
    return tot_pompe_attive_adesso > tot_pompe_attive_necessarie_max


def calcola_tot_pompe_attive_necessarie_min(livello_attuale: float,
                                            soglie: list[tuple[float, float]],
                                            num_pompe_per_soglia: int) -> int:

    soglia_attivazione_piu_alta_raggiunta: int = calcola_soglia_attivazione_piu_alta_raggiunta(livello_attuale, soglie)

    # Il numero di pompe minime necessarie in questo istante
    # è dato dalla sequenza della soglia di attivazione raggiunta dal livello d'acqua,
    # moltiplicato quante soglie si desiderano alla raggiunta di ogni soglia
    # Ad esempio, se sono poco oltre la soglia attivazione 2,
    # e bisogna attivare una pompa al raggiungimento della soglia di attivazione 2,
    # allora il numero di pompe attive necessarie minimo è 2*1 = 2
    return soglia_attivazione_piu_alta_raggiunta * num_pompe_per_soglia



def calcola_tot_pompe_attive_necessarie_max(livello_attuale: float,
                                            soglie: list[tuple[float, float]],
                                            num_pompe_per_soglia: int) -> int:

    soglia_disattivazione_piu_bassa_raggiunta: int = calcola_soglia_disattivazione_piu_bassa_raggiunta(livello_attuale, soglie)

    # Il numero massimo di pompe massime necessarie in questo momento
    # è dato dalla soglia di disattivazione più bassa raggiunta dal livello d'acqua.
    # Nello specifico, si considera la soglia precedente,
    # e si moltiplicano il numero di soglie per ogni soglia di disattivazione raggiunta.
    # Ad esempio, se il livello d'acqua ha raggiunto il livello di disattivazione 5, allora è certo
    # che non ci possono essere più di (5-1)*1 = 4 pompe attive attive in questo momento,
    # e questo definisce il numero di pompe attive necessarie massimo.
    return (soglia_disattivazione_piu_bassa_raggiunta - 1) * num_pompe_per_soglia



def calcola_soglia_attivazione_piu_alta_raggiunta(livello_attuale: float,
                                                 soglie: list[tuple[float, float]]) -> int:
    """
    :param livello_attuale: Il livello attuale dell'acqua.
    :param soglie: Le soglie.
    :return: La sequenza della soglia di attivazione più alta raggiunta, a partire da 1.
            0 significa che nessuna soglia di attivazione è stata raggiunta, e che quindi
            il livello attuale è sotto la prima soglia di attivazione.
    """

    # Sequenza di soglia attivazione più alta raggiunta
    # Perché si inizializza a zero? Se non viene
    # raggiunta nessuna soglia di attivazione (e quindi il loop non aggiorna mai questo valore)
    # allora si assume che la soglia di attivazione più alta raggiunta è la soglia 0,
    # cioè il livello acqua è "sotto la prima soglia di attivazione".
    soglia_attivazione_piu_alta: int = 0

    # Da sinistra verso destra, quindi dalla soglia più bassa a quella più alta:
    # LOGICA 1: La più alta soglia di attivazione raggiunta è
    # la precedente della prima soglia di attivazione non raggiunta.
    for i in range(len(soglie)):

        soglia_attivazione, _ = soglie[i]

        # Se il livello attuale supera questa soglia attivazione,
        # aggiorna la soglia attivazione più alta finora
        if livello_attuale >= soglia_attivazione:
            # "i+1" significa "la sequenza della soglia attuale",
            # visto che l'indice parte da zero ma le soglie vengono numerate a partire da 1
            soglia_attivazione_piu_alta = i+1
        # Alla prima volta che il livello attuale non supera una soglia attivazione, esci.
        # Uscendo, rimane comunque la soglia attivazione più alta raggiunta finora;
        # questa è l'implementazione della LOGICA 1.
        else:
            break

    return soglia_attivazione_piu_alta


def calcola_soglia_disattivazione_piu_bassa_raggiunta(livello_attuale: float,
                                                     soglie: list[tuple[float, float]]) -> int:
    """
    :param livello_attuale: Il livello attuale dell'acqua.
    :param soglie: Le soglie.
    :return: La sequenza della soglia di disattivazione più bassa raggiunta, a partire da 1.
             Per rappresentare numericamente che non esiste, tra quelle date,
             una soglia di disattivazione più bassa raggiunta, e cioè che il livello
             è oltre l'ultima soglia di disattivazione (quindi si assume
             un livello abbastanza alto) viene calcolata il numero di soglie + 1.
    """

    # Sequenza di soglia disattivazione più bassa raggiunta.
    # Perché si inizializza al numero di soglie + 1?
    # Se non viene raggiunta nessuna soglia di disattivazione (e quindi il loop non aggiorna mai questo valore)
    # allora si assume che la soglia di disattivazione più bassa raggiunta sia "quella dopo l'ultima",
    # cioè il numero di soglie + 1.
    soglia_disattivazione_piu_bassa: int = len(soglie)+1

    # Da sinistra verso destra, quindi dalla soglia più bassa a quella più alta:
    # La più bassa soglia di disattivazione raggiunta è
    # la prima soglia di disattivazione ad essere raggiunta.
    for i in range(len(soglie)):

        _, soglia_disattivazione = soglie[i]

        # Se il livello attuale è minore di questa soglia disattivazione,
        # aggiorna la soglia disattivazione ed esci subito.
        if livello_attuale < soglia_disattivazione:
            # "i+1" significa "la sequenza della soglia attuale"
            soglia_disattivazione_piu_bassa = i+1
            break

    return soglia_disattivazione_piu_bassa