from src.algo import calcola_soglia_attivazione_piu_alta_raggiunta


def test_data_UnaSoglia_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_SogliaAttivazionePiuAltaEZero():
    livello_attuale = 40
    soglie = [
        (60, 50)
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 0


def test_data_DueSoglie_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_SogliaAttivazionePiuAltaEZero():
    livello_attuale = 40
    soglie = [
        (60, 50),
        (70, 65),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 0


def test_data_TreSoglie_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_SogliaAttivazionePiuAltaEZero():
    livello_attuale = 40
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 0




def test_data_UnaSoglia_quando_LivelloAttualeESuperioreAPrimaSoglia_allora_SogliaAttivazionePiuAltaEUno():
    livello_attuale = 65
    soglie = [
        (60, 50)
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 1


def test_data_DueSoglie_quando_LivelloAttualeESuperioreAPrimaSoglia_allora_SogliaAttivazionePiuAltaEUno():
    livello_attuale = 65
    soglie = [
        (60, 50),
        (70, 65),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 1


def test_data_TreSoglie_quando_LivelloAttualeESuperioreAPrimaSoglia_allora_SogliaAttivazionePiuAltaEUno():
    livello_attuale = 65
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 1


def test_data_DueSoglie_quando_LivelloAttualeESuperioreASecondaSoglia_allora_SogliaAttivazionePiuAltaEDue():
    livello_attuale = 75
    soglie = [
        (60, 50),
        (70, 65),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 2


def test_data_TreSoglie_quando_LivelloAttualeESuperioreASecondaSoglia_allora_SogliaAttivazionePiuAltaEDue():
    livello_attuale = 75
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 2


def test_data_TreSoglie_quando_LivelloAttualeESuperioreATerzaSoglia_allora_SogliaAttivazionePiuAltaETre():
    livello_attuale = 85
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 3


def test_data_QuattroSoglie_quando_LivelloAttualeESuperioreATerzaSoglia_allora_SogliaAttivazionePiuAltaETre():
    livello_attuale = 85
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 85),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 3


def test_data_QuattroSoglie_quando_LivelloAttualeESuperioreAQuartaSoglia_allora_SogliaAttivazionePiuAltaEQuattro():
    livello_attuale = 95
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 85),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 4

def test_data_CinqueSoglie_quando_LivelloAttualeESuperioreAQuartaSoglia_allora_SogliaAttivazionePiuAltaEQuattro():
    livello_attuale = 95
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 85),
        (96, 91),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 4


def test_data_CinqueSoglie_quando_LivelloAttualeESuperioreAQuintaSoglia_allora_SogliaAttivazionePiuAltaECinque():
    livello_attuale = 96
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 85),
        (96, 91),
    ]

    soglia_attivazione_piu_alta = calcola_soglia_attivazione_piu_alta_raggiunta(
        livello_attuale,
        soglie,
    )

    assert soglia_attivazione_piu_alta == 5