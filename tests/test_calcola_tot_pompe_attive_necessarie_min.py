from src.algo import calcola_tot_pompe_attive_necessarie_min


def test_data_UnaSoglia_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_TotPompeAttiveNecessarieMinEZero():
    livello_attuale = 40
    soglie = [
        (60, 50)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_min(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 0


def test_data_DueSoglie_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_TotPompeAttiveNecessarieMinEZero():
    livello_attuale = 40
    soglie = [
        (60, 50),
        (70, 60)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_min(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 0


def test_data_DueSoglie_quando_LivelloAttualeESuperioreAPrimaSoglia_allora_TotPompeAttiveNecessarieMinEUno():
    livello_attuale = 65
    soglie = [
        (60, 50),
        (70, 60)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_min(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 1



def test_data_DueSoglie_quando_LivelloAttualeESuperioreASecondaSoglia_allora_TotPompeAttiveNecessarieMinEDue():
    livello_attuale = 75
    soglie = [
        (60, 50),
        (70, 60)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_min(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 2



def test_data_TreSoglie_quando_LivelloAttualeESuperioreASecondaSoglia_allora_TotPompeAttiveNecessarieMinEDue():
    livello_attuale = 75
    soglie = [
        (60, 50),
        (70, 60),
        (80, 70)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_min(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 2
