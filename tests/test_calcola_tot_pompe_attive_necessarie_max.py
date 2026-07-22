from src.lib.algo import calcola_tot_pompe_attive_necessarie_max


def test_data_UnaSoglia_quando_LivelloAttualeEInferioreASogliaPiuBassa_allora_TotPompeAttiveNecessarieMaxEZero():
    livello_attuale = 40
    soglie = [
        (60, 50)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 0


def test_data_UnaSoglia_quando_LivelloAttualeESuperioreASogliaPiuAlta_allora_TotPompeAttiveNecessarieMaxEUno():
    """
                                      1 (60)
                                      |
    SOGLIE         --------------------------------------
    ATTIVAZ.                          |
                                      |
    SOGLIE         --------------------------------------
    DISATTIVAZ.          |            |       |
                       1 (50)         |       |
                         |            |       |
    LIVELLO              |            |      (70)
    ATTUALE              |            |
                         |            |
    MIN POMPE       0    |    0       |       1
    ATTIVE               |            |
                         |            |
    MAX POMPE       0    |    1       |       1
    ATTIVE

    """

    livello_attuale = 70
    soglie = [
        (60, 50)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 1



def test_data_UnaSoglia_quando_LivelloAttualeEAMetaTraSoglie_allora_TotPompeAttiveNecessarieMaxEUno():
    """
                                      1 (60)
                                      |
    SOGLIE         --------------------------------------
    ATTIVAZ.                          |
                                      |
    SOGLIE         --------------------------------------
    DISATTIVAZ.          |      |     |
                       1 (50)   |     |
                         |      |     |
    LIVELLO              |     (65)   |
    ATTUALE              |            |
                         |            |
    MIN POMPE       0    |    0       |       1
    ATTIVE               |            |
                         |            |
    MAX POMPE       0    |    1       |       1
    ATTIVE

    """

    livello_attuale = 65
    soglie = [
        (60, 50)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 1


def test_data_DueSoglie_quando_LivelloAttualeEAMetaTraSoglie_allora_TotPompeAttiveNecessarieMaxEUno():
    """
                                      1 (60)           2 (70)
                                      |                |
    SOGLIE         -------------------------------------------
    ATTIVAZ.                          |                |
                                      |                |
    SOGLIE         -------------------------------------------
    DISATTIVAZ.          |            |    |   |       |
                       1 (50)         |    |   2 (65)  |
                         |            |    |   |       |
    LIVELLO              |            |   (64) |       |
    ATTUALE              |            |        |       |
                         |            |        |       |
    MIN POMPE       0    |    0       |  1     |  1    |   2
    ATTIVE               |            |        |       |
                         |            |        |       |
    MAX POMPE       0    |    1       |  1     |  2    |   2
    ATTIVE

    """

    livello_attuale = 64
    soglie = [
        (60, 50),
        (70, 65),
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 1


def test_data_DueSoglie_quando_LivelloAttualeEAMetaTraSoglie_allora_TotPompeAttiveNecessarieMaxEDue():
    """
                                      1 (60)          2 (70)
                                      |               |
    SOGLIE         -------------------------------------------
    ATTIVAZ.                          |               |
                                      |               |
    SOGLIE         -------------------------------------------
    DISATTIVAZ.          |            |       |   |   |
                       1 (50)         |    2 (65) |   |
                         |            |       |   |   |
    LIVELLO              |            |       |  (66) |
    ATTUALE              |            |       |       |
                         |            |       |       |
    MIN POMPE       0    |    0       |  1    |  1    |   2
    ATTIVE               |            |       |       |
                         |            |       |       |
    MAX POMPE       0    |    1       |  1    |  2    |   2
    ATTIVE

    """

    livello_attuale = 66
    soglie = [
        (60, 50),
        (70, 65),
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 2


def test_data_DueSoglie_quando_LivelloAttualeEAMetaTraSoglie_allora_TotPompeAttiveNecessarieMaxEDue_2():
    """
                                      1 (60)          2 (70)
                                      |               |
    SOGLIE         -------------------------------------------
    ATTIVAZ.                          |               |
                                      |               |
    SOGLIE         -------------------------------------------
    DISATTIVAZ.          |            |       |       |  |
                       1 (50)         |    2 (65)     |  |
                         |            |       |       |  |
    LIVELLO              |            |       |       | (71)
    ATTUALE              |            |       |       |
                         |            |       |       |
    MIN POMPE       0    |    0       |  1    |  1    |   2
    ATTIVE               |            |       |       |
                         |            |       |       |
    MAX POMPE       0    |    1       |  1    |  2    |   2
    ATTIVE

    """

    livello_attuale = 71
    soglie = [
        (60, 50),
        (70, 65),
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 2



def test_data_DueSoglie_quando_LivelloAttualeEIlPiuBasso_allora_TotPompeAttiveNecessarieMaxEZero():
    """
                                      1 (60)          2 (70)
                                      |               |
    SOGLIE         -------------------------------------------
    ATTIVAZ.                          |               |
                                      |               |
    SOGLIE         -------------------------------------------
    DISATTIVAZ.      |    |            |       |       |
                     |  1 (50)         |    2 (65)     |
                     |    |            |       |       |
    LIVELLO         (49)  |            |       |       |
    ATTUALE               |            |       |       |
                          |            |       |       |
    MIN POMPE       0     |    0       |  1    |  1    |   2
    ATTIVE                |            |       |       |
                          |            |       |       |
    MAX POMPE       0     |    1       |  1    |  2    |   2
    ATTIVE

    """

    livello_attuale = 49
    soglie = [
        (60, 50),
        (70, 65),
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 0


def test_data_TreSoglie_quando_LivelloAttualeETraSoglie_allora_TotPompeAttiveNecessarieMaxEDue():
    """
                                      1 (60)          2 (70)         3 (80)
                                      |               |              |
    SOGLIE         ---------------------------------------------------------
    ATTIVAZ.                          |               |              |
                                      |               |              |
    SOGLIE         --------------------------------------------------------
    DISATTIVAZ.          |            |       |       |    |   |     |
                       1 (50)         |    2 (65)     |    |  3 (75) |
                         |            |       |       |    |   |     |
    LIVELLO              |            |       |       |   (74) |     |
    ATTUALE              |            |       |       |        |     |
                         |            |       |       |        |     |
    MIN POMPE       0    |    0       |  1    |  1    |   2    |  2  |  3
    ATTIVE               |            |       |       |        |     |
                         |            |       |       |        |     |
    MAX POMPE       0    |    1       |  1    |  2    |   2    |  3  |  3
    ATTIVE

    """

    livello_attuale = 74
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 2



def test_data_TreSoglie_quando_LivelloAttualeETraSoglie_allora_TotPompeAttiveNecessarieMaxETre():
    """
                                      1 (60)          2 (70)         3 (80)
                                      |               |              |
    SOGLIE         ---------------------------------------------------------
    ATTIVAZ.                          |               |              |
                                      |               |              |
    SOGLIE         --------------------------------------------------------
    DISATTIVAZ.          |            |       |       |       |  |   |
                       1 (50)         |    2 (65)     |   3 (75) |   |
                         |            |       |       |       |  |   |
    LIVELLO              |            |       |       |       | (76) |
    ATTUALE              |            |       |       |       |      |
                         |            |       |       |       |      |
    MIN POMPE       0    |    0       |  1    |  1    |   2   |  2   |  3
    ATTIVE               |            |       |       |       |      |
                         |            |       |       |       |      |
    MAX POMPE       0    |    1       |  1    |  2    |   2   |  3   |  3
    ATTIVE

    """

    livello_attuale = 76
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 3


def test_data_QuattroSoglie_quando_LivelloAttualeETraSoglie_allora_TotPompeAttiveNecessarieMaxETre():
    """
                                      1 (60)          2 (70)                 3 (80)      4 (90)
                                      |               |                      |           |
    SOGLIE         -----------------------------------------------------------------------------
    ATTIVAZ.                          |               |                      |           |
                                      |               |                      |           |
    SOGLIE         -----------------------------------------------------------------------------
    DISATTIVAZ.          |            |       |       |       |  |    |      |           |
                       1 (50)         |    2 (65)     |   3 (75) |   4(78)   |           |
                         |            |       |       |       |  |    |      |           |
    LIVELLO              |            |       |       |       | (76)  |      |           |
    ATTUALE              |            |       |       |       |       |      |           |
                         |            |       |       |       |       |      |           |
    MIN POMPE       0    |    0       |  1    |  1    |   2   |   2   |  2   |   3       |   4
    ATTIVE               |            |       |       |       |       |      |           |
                         |            |       |       |       |       |      |           |
    MAX POMPE       0    |    1       |  1    |  2    |   2   |   3   |  4   |   4       |   4
    ATTIVE

    """

    livello_attuale = 76
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 3


def test_data_QuattroSoglie_quando_LivelloAttualeETraSoglie_allora_TotPompeAttiveNecessarieMaxEQuattro():
    """
                                      1 (60)          2 (70)                    3 (80)      4 (90)
                                      |               |                         |           |
    SOGLIE         -----------------------------------------------------------------------------
    ATTIVAZ.                          |               |                         |           |
                                      |               |                         |           |
    SOGLIE         -----------------------------------------------------------------------------
    DISATTIVAZ.          |            |       |       |       |       |     |   |           |
                       1 (50)         |    2 (65)     |   3 (75)     4(78)  |   |           |
                         |            |       |       |       |       |     |   |           |
    LIVELLO              |            |       |       |       |       |   (79)  |           |
    ATTUALE              |            |       |       |       |       |         |           |
                         |            |       |       |       |       |         |           |
    MIN POMPE       0    |    0       |  1    |  1    |   2   |   2   |  2      |   3       |   4
    ATTIVE               |            |       |       |       |       |         |           |
                         |            |       |       |       |       |         |           |
    MAX POMPE       0    |    1       |  1    |  2    |   2   |   3   |  4      |   4       |   4
    ATTIVE

    """

    livello_attuale = 79
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 4



def test_data_QuattroSoglie_quando_LivelloAttualeETraSoglie_allora_TotPompeAttiveNecessarieMaxEDue():
    """
                                      1 (60)          2 (70)                     3 (80)      4 (90)
                                      |               |                          |           |
    SOGLIE         -----------------------------------------------------------------------------
    ATTIVAZ.                          |               |                          |           |
                                      |               |                          |           |
    SOGLIE         -----------------------------------------------------------------------------
    DISATTIVAZ.          |            |       |       |  |     |       |         |           |
                       1 (50)         |    2 (65)     |  |     3 (75)  4(78)     |           |
                         |            |       |       |  |     |       |         |           |
    LIVELLO              |            |       |       | (71)   |       |         |           |
    ATTUALE              |            |       |       |        |       |         |           |
                         |            |       |       |        |       |         |           |
    MIN POMPE       0    |    0       |  1    |  1    |   2    |   2   |  2      |   3       |   4
    ATTIVE               |            |       |       |        |       |         |           |
                         |            |       |       |        |       |         |           |
    MAX POMPE       0    |    1       |  1    |  2    |   2    |   3   |  4      |   4       |   4
    ATTIVE

    """

    livello_attuale = 71
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    num_pompe_per_soglia = 1

    tot_pompe_attive_necessarie_min = calcola_tot_pompe_attive_necessarie_max(
        livello_attuale,
        soglie,
        num_pompe_per_soglia
    )

    assert tot_pompe_attive_necessarie_min == 2