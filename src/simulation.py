from datetime import datetime
from collections.abc import Callable
from enum import Enum
import csv
import os

from src.lib.machine import run_machine_in_loop
from src.lib.algo import decidi_se_attivare_o_disattivare_pompe
from src.lib.utils import ottieni_livello_variato


class StatoMacchina(Enum):
    INIT = 0,
    MACCHINA_ATTIVA = 1,
    MACCHINA_FERMA = 2,
    ATTIVA_PROSSIMA_POMPA = 3,
    DISATTIVA_ULTIMA_POMPA = 4


def machine_func(M: dict, on_iteration_end: Callable):
    """
    :param on_iteration_end:
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

    on_iteration_end(M)



REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

LOG_FILENAME = os.path.join(REPORTS_DIR, f"machine_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

def on_iteration_end_(M: dict):
    file_esiste = os.path.isfile(LOG_FILENAME)
    with open(LOG_FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_esiste:
            writer.writerow(["stato", "livello_acqua", "tot_pompe_attive"])
        writer.writerow([M["stato"], M["livello_acqua"], M["tot_pompe_attive"]])


# MODIFICARE QUI

run_machine_in_loop(machine_func, {
    "stato": StatoMacchina.INIT,
    "livello_acqua": 60,
    "pompaA": {
        "attiva": False
    },
    "soglie": [
        (40, 25),
        (50, 35),
        (60, 40),
        (70, 50),
        (80, 60),
        (90, 60),
    ],
    "tot_pompe_attive": 0
}, on_iteration_end_)