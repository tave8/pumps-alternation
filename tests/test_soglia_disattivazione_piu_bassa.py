from src.main import calcola_soglia_disattivazione_piu_bassa_raggiunta


def test_data_UnaSoglia_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_SogliaDisattivazionePiuBassaEUno():
    livello_attuale = 40
    soglie = [
        (60, 50)
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 1


def test_data_DueSoglie_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_SogliaDisattivazionePiuBassaEUno():
    livello_attuale = 40
    soglie = [
        (60, 50),
        (70, 65)
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 1


def test_data_TreSoglie_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_SogliaDisattivazionePiuBassaEUno():
    livello_attuale = 40
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75)
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 1


def test_data_UnaSoglia_quando_LivelloAttualeESuperioreASogliaPiuAlta_allora_SogliaDisattivazionePiuBassaEDue():
    livello_attuale = 55
    soglie = [
        (60, 50)
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 2


def test_data_DueSoglie_quando_LivelloAttualeESuperioreASogliaPiuAlta_allora_SogliaDisattivazionePiuBassaEDue():
    livello_attuale = 55
    soglie = [
        (60, 50),
        (70, 65),
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 2


def test_data_TreSoglie_quando_LivelloAttualeESuperioreASogliaPiuBassa_allora_SogliaDisattivazionePiuBassaEUno():
    livello_attuale = 45
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 1


def test_data_TreSoglie_quando_LivelloAttualeESuperioreASogliaPiuAlta_allora_SogliaDisattivazionePiuBassaEQuattro():
    livello_attuale = 76
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 4


def test_data_TreSoglie_quando_LivelloAttualeEInferioreATerzaSoglia_allora_SogliaDisattivazionePiuBassaETre():
    livello_attuale = 74
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 3



def test_data_QuattroSoglie_quando_LivelloAttualeEInferioreAQuartaSoglia_allora_SogliaDisattivazionePiuBassaEQuattro():
    livello_attuale = 84
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 85),
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 4


def test_data_QuattroSoglie_quando_LivelloAttualeESuperioreAPiuBasso_allora_SogliaDisattivazionePiuBassaECinque():
    livello_attuale = 86
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 85),
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 5


def test_data_CinqueSoglie_quando_LivelloAttualeEInferioreAQuintaSoglia_allora_SogliaDisattivazionePiuBassaECinque():
    livello_attuale = 91
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 85),
        (95, 92),
    ]

    soglia_disattivazione_piu_bassa = calcola_soglia_disattivazione_piu_bassa_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_disattivazione_piu_bassa == 5