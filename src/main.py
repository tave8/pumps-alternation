from enum import Enum

from src.lib.machine import run_machine_in_loop
from src.lib.pump_logic import decidi_se_attivare_o_disattivare_pompe
from src.lib.utils import ottieni_livello_variato


class StatoMacchina(Enum):
    INIT = 0,
    MACCHINA_ATTIVA = 1,
    MACCHINA_FERMA = 2,
    ATTIVA_PROSSIMA_POMPA = 3,
    DISATTIVA_ULTIMA_POMPA = 4


def machine_func(M: dict):
    """
    :param M: machine memory - persists across iterations
    """

    # Varia il livello dell'acqua casualmente
    M["livello_acqua"] = ottieni_livello_variato(M["livello_acqua"], 0, 100)

    match M["stato"]:
        case StatoMacchina.INIT:
            M["stato"] = StatoMacchina.MACCHINA_ATTIVA
            print("macchina in stato iniziale")

        case StatoMacchina.MACCHINA_ATTIVA:
            decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
                M["livello_acqua"],
                M["soglie"],
                M["tot_pompe_attive"]
            )

            if decisione_attiva_pompa:
                M["stato"] = StatoMacchina.ATTIVA_PROSSIMA_POMPA
            elif decisione_disattiva_pompa:
                M["stato"] = StatoMacchina.DISATTIVA_ULTIMA_POMPA

            print("macchina attiva")

        case StatoMacchina.ATTIVA_PROSSIMA_POMPA:
            M["pompaA"]["attiva"] = True
            M["tot_pompe_attive"] += 1

            M["stato"] = StatoMacchina.MACCHINA_ATTIVA
            print("attivazione prossima pompa")

        case StatoMacchina.DISATTIVA_ULTIMA_POMPA:
            M["pompaA"]["attiva"] = False
            M["tot_pompe_attive"] -= 1
            M["stato"] = StatoMacchina.MACCHINA_ATTIVA
            print("disattivazione ultima pompa")


    print("livello acqua: ", M["livello_acqua"])
    print("tot pompe attive: ", M["tot_pompe_attive"])
    print("------------------------------")

    # print("machine memory: ", M)



run_machine_in_loop(machine_func, {
    "stato": StatoMacchina.INIT,
    "livello_acqua": 70,
    "pompaA": {
        "attiva": False
    },
    "soglie": [
        (60, 55),
        (70, 65),
        (80, 75),
        (90, 85)
    ],
    "tot_pompe_attive": 0
})