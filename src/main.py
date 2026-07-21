def decidi_se_attivare_o_disattivare_pompe(livello_attuale: float,
                                           soglie: list[tuple[float, float]],
                                           tot_pompe_attive_adesso: int) -> tuple[bool, bool]:
    """
    L'ordine in cui vengono passate le soglia conta.
    Si devono passare le soglie dalla più bassa alla più alta.
    Esempio:
        (60, 55)
        (70, 65)
        (80, 75)

    Che rappresenta, concettualmente:

        Soglia attivazione   |    Soglia disattivazione   |   Numero sequenziale (auto-assegnato)
        ------------------------------------------------------------------------------------------
             60                          55                        1
             70                          65                        2
             80                          75                        3


    :param livello_attuale:
    :param soglie:
    :param tot_pompe_attive_adesso:
    :return:
    """

    num_pompe_per_soglia: int = 1

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

    return decisione_attiva_pompa, decisione_disattiva_pompa


def ci_sono_poche_pompe_attive(livello_attuale: float,
                               soglie: list[tuple[float, float]],
                               tot_pompe_attive_adesso: int,
                               num_pompe_per_soglia: int) -> bool:

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_min(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

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

    return tot_pompe_attive_adesso > tot_pompe_attive_necessarie_max


def calcola_tot_pompe_attive_necessarie_min(livello_attuale: float,
                                            soglie: list[tuple[float, float]],
                                            num_pompe_per_soglia: int) -> int:

    soglia_attivazione_piu_alta_raggiunta: int = calcola_soglia_attivazione_piu_alta_raggiunta(livello_attuale, soglie)

    return soglia_attivazione_piu_alta_raggiunta * num_pompe_per_soglia



def calcola_tot_pompe_attive_necessarie_max(livello_attuale: float,
                                            soglie: list[tuple[float, float]],
                                            num_pompe_per_soglia: int) -> int:

    soglia_disattivazione_piu_bassa_raggiunta: int = calcola_soglia_disattivazione_piu_bassa_raggiunta(livello_attuale, soglie)

    return (soglia_disattivazione_piu_bassa_raggiunta - 1) * num_pompe_per_soglia



def calcola_soglia_attivazione_piu_alta_raggiunta(livello_attuale: float,
                                                 soglie: list[tuple[float, float]]) -> int:
    """
    :param livello_attuale:
    :param soglie:
    :return:
    """
    # Sequenza di soglia attivazione più alta raggiunta
    seq_soglia_attivazione_piu_alta: int = 0

    #     Da sinistra verso destra, quindi dalla soglia più bassa a quella più alta:
    #     La più alta soglia di attivazione raggiunta è
    #     la precedente della prima soglia di attivazione non raggiunta
    for idx in range(len(soglie)):
        (soglia_attivazione,
         soglia_disattivazione) = soglie[idx]

        # Se il livello attuale supera questa soglia attivazione,
        # aggiorna la soglia attivazione più alta finora
        if livello_attuale >= soglia_attivazione:
            # "idx+1" significa "la sequenza della soglia attuale"
            seq_soglia_attivazione_piu_alta = idx+1
        # Alla prima volta che il livello attuale non supera una soglia attivazione,
        # esci ritornando la soglia attivazione più alta finora
        else:
            break

    return seq_soglia_attivazione_piu_alta


def calcola_soglia_disattivazione_piu_bassa_raggiunta(livello_attuale: float,
                                                     soglie: list[tuple[float, float]]) -> int:
    # Sequenza di soglia disattivazione più bassa raggiunta
    seq_soglia_disattivazione_piu_bassa: int = len(soglie)+1

    #     Da sinistra verso destra, quindi dalla soglia più bassa a quella più alta:
    #     La più bassa soglia di disattivazione raggiunta è
    #     la prima soglia di disattivazione ad essere vera
    for idx in range(len(soglie)):
        (soglia_attivazione,
         soglia_disattivazione) = soglie[idx]

        # Se il livello attuale è minore di questa soglia disattivazione,
        # aggiorna la soglia disattivazione ed esci subito
        if livello_attuale < soglia_disattivazione:
            # "idx+1" significa "la sequenza della soglia attuale"
            seq_soglia_disattivazione_piu_bassa = idx+1
            break

    return seq_soglia_disattivazione_piu_bassa