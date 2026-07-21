from src.main import decidi_se_attivare_o_disattivare_pompe


def test_data_ZeroPompeAttive_quando_LivelloEIlPiuBasso_allora_NessunaDecisione():
    """
                                      1 (60)
                                      |
    SOGLIE         --------------------------------------
    ATTIVAZ.                          |
                                      |
    SOGLIE         --------------------------------------
    DISATTIVAZ.     |     |           |
                    |   1 (50)        |
                    |     |           |
    LIVELLO       (40)    |           |
    ATTUALE               |           |
                          |           |
    MIN POMPE       0     |    0      |       1
    ATTIVE                |           |
                          |           |
    MAX POMPE       0     |    1      |       1
    ATTIVE

    TOT POMPE       0
    ATTIVE

    """

    livello_attuale = 40
    soglie = [
        (60, 50)
    ]
    tot_pompe_attive_adesso = 0

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa


def test_data_UnaPompeAttive_quando_LivelloEIlPiuBasso_allora_DisattivaPompa():
    """
                                      1 (60)
                                      |
    SOGLIE         --------------------------------------
    ATTIVAZ.                          |
                                      |
    SOGLIE         --------------------------------------
    DISATTIVAZ.     |     |           |
                    |   1 (50)        |
                    |     |           |
    LIVELLO       (40)    |           |
    ATTUALE               |           |
                          |           |
    MIN POMPE       0     |    0      |       1
    ATTIVE                |           |
                          |           |
    MAX POMPE       0     |    1      |       1
    ATTIVE

    TOT POMPE       1
    ATTIVE

    """
    livello_attuale = 40
    soglie = [
        (60, 50)
    ]
    tot_pompe_attive_adesso = 1

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa




def test_data_ZeroPompeAttive_quando_LivelloEInRange_allora_NessunaDecisione_2():
    """
                                       1 (60)
                                       |
    SOGLIE         --------------------------------------
    ATTIVAZ.                           |
                                       |
    SOGLIE         --------------------------------------
    DISATTIVAZ.           |     |      |
                       1 (50)   |      |
                          |     |      |
    LIVELLO               |    (55)    |
    ATTUALE               |            |
                          |            |
    MIN POMPE       0     |    0       |       1
    ATTIVE                |            |
                          |            |
    MAX POMPE       0     |    1       |       1
    ATTIVE

    TOT POMPE                  0
    ATTIVE

    """
    livello_attuale = 55
    soglie = [
        (60, 50)
    ]
    tot_pompe_attive_adesso = 0

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_UnaPompeAttive_quando_LivelloEInRange_allora_NessunaDecisione_2():
    """
                                       1 (60)
                                       |
    SOGLIE         --------------------------------------
    ATTIVAZ.                           |
                                       |
    SOGLIE         --------------------------------------
    DISATTIVAZ.           |     |      |
                       1 (50)   |      |
                          |     |      |
    LIVELLO               |    (55)    |
    ATTUALE               |            |
                          |            |
    MIN POMPE       0     |    0       |       1
    ATTIVE                |            |
                          |            |
    MAX POMPE       0     |    1       |       1
    ATTIVE

    TOT POMPE                  1
    ATTIVE

    """
    livello_attuale = 55
    soglie = [
        (60, 50)
    ]
    tot_pompe_attive_adesso = 1

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_DuePompeAttive_quando_LivelloEInRange_allora_DisattivaPompa():
    """
                                       1 (60)
                                       |
    SOGLIE         --------------------------------------
    ATTIVAZ.                           |
                                       |
    SOGLIE         --------------------------------------
    DISATTIVAZ.           |     |      |
                       1 (50)   |      |
                          |     |      |
    LIVELLO               |    (55)    |
    ATTUALE               |            |
                          |            |
    MIN POMPE       0     |    0       |       1
    ATTIVE                |            |
                          |            |
    MAX POMPE       0     |    1       |       1
    ATTIVE

    TOT POMPE                  2
    ATTIVE

    """
    livello_attuale = 55
    soglie = [
        (60, 50)
    ]
    tot_pompe_attive_adesso = 2

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa




def test_data_ZeroPompeAttive_quando_LivelloEIlPiuAlto_allora_AttivaPompa():
    """
                                       1 (60)
                                       |
    SOGLIE         --------------------------------------
    ATTIVAZ.                           |
                                       |
    SOGLIE         --------------------------------------
    DISATTIVAZ.           |            |      |
                       1 (50)          |      |
                          |            |      |
    LIVELLO               |            |     (65)
    ATTUALE               |            |
                          |            |
    MIN POMPE       0     |    0       |       1
    ATTIVE                |            |
                          |            |
    MAX POMPE       0     |    1       |       1
    ATTIVE

    TOT POMPE                                  0
    ATTIVE

    """
    livello_attuale = 65
    soglie = [
        (60, 50)
    ]
    tot_pompe_attive_adesso = 0

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_DuePompeAttive_quando_LivelloEIlPiuAlto_allora_DisattivaPompa():
    """
                                       1 (60)
                                       |
    SOGLIE         --------------------------------------
    ATTIVAZ.                           |
                                       |
    SOGLIE         --------------------------------------
    DISATTIVAZ.           |            |      |
                       1 (50)          |      |
                          |            |      |
    LIVELLO               |            |     (65)
    ATTUALE               |            |
                          |            |
    MIN POMPE       0     |    0       |       1
    ATTIVE                |            |
                          |            |
    MAX POMPE       0     |    1       |       1
    ATTIVE

    TOT POMPE                                  2
    ATTIVE

    """
    livello_attuale = 65
    soglie = [
        (60, 50)
    ]
    tot_pompe_attive_adesso = 2

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa





def test_data_ZeroPompeAttive_quando_LivelloEInRange_allora_AttivaPompa():
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

    TOT POMPE                            0
    ATTIVE

    """

    livello_attuale = 64
    soglie = [
        (60, 50),
        (70, 65),
    ]
    tot_pompe_attive_adesso = 0

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_UnaPompeAttive_quando_LivelloEInRange_allora_NessunaDecisione():
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

    TOT POMPE                                    1
    ATTIVE

    """

    livello_attuale = 66
    soglie = [
        (60, 50),
        (70, 65),
    ]
    tot_pompe_attive_adesso = 1

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa


def test_data_DuePompeAttive_quando_LivelloEInRange_allora_NessunaDecisione():
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

    TOT POMPE                                    2
    ATTIVE

    """

    livello_attuale = 66
    soglie = [
        (60, 50),
        (70, 65),
    ]
    tot_pompe_attive_adesso = 2

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_ZeroPompeAttive_quando_LivelloEInRange_allora_AttivaPompa_2():
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

    TOT POMPE                                    0
    ATTIVE

    """

    livello_attuale = 66
    soglie = [
        (60, 50),
        (70, 65),
    ]
    tot_pompe_attive_adesso = 0

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_TrePompeAttive_quando_LivelloEInRange_allora_DisattivaPompa_2():
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

    TOT POMPE                                    3
    ATTIVE

    """

    livello_attuale = 66
    soglie = [
        (60, 50),
        (70, 65),
    ]
    tot_pompe_attive_adesso = 3

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa


def test_data_QuattroPompeAttive_quando_LivelloEInRange_allora_DisattivaPompa_2():
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

    TOT POMPE                                    4
    ATTIVE

    """

    livello_attuale = 66
    soglie = [
        (60, 50),
        (70, 65),
    ]
    tot_pompe_attive_adesso = 4

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa



def test_data_UnaPompeAttive_quando_LivelloEInRange_allora_AttivaPompa():
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

    TOT POMPE                                             1
    ATTIVE

    """

    livello_attuale = 74
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75)
    ]
    tot_pompe_attive_adesso = 1

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_DuePompeAttive_quando_LivelloEInRange_allora_NessunaDecisione_2():
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

    TOT POMPE                                             2
    ATTIVE

    """

    livello_attuale = 74
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75)
    ]
    tot_pompe_attive_adesso = 2

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa




def test_data_TrePompeAttive_quando_LivelloEInRange_allora_DisattivaPompa():
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

    TOT POMPE                                             3
    ATTIVE

    """

    livello_attuale = 74
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75)
    ]
    tot_pompe_attive_adesso = 3

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa


def test_data_TrePompeAttive_quando_LivelloEInRange_allora_NessunaDecisione():
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

    TOT POMPE                                                     3
    ATTIVE

    """

    livello_attuale = 76
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 3

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa


def test_data_UnaPompeAttive_quando_LivelloEInRange_allora_AttivaPompa_2():
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

    TOT POMPE                                                     1
    ATTIVE

    """

    livello_attuale = 76
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 1

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert decisione_attiva_pompa
    assert not decisione_disattiva_pompa



def test_data_QuattrePompeAttive_quando_LivelloEInRange_allora_DisattivaPompa():
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

    TOT POMPE                                                     4
    ATTIVE

    """

    livello_attuale = 76
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 4

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa





def test_data_TrePompeAttive_quando_LivelloEInRange_allora_NessunaDecisione_2():
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

    TOT POMPE                                                            3
    ATTIVE

    """

    livello_attuale = 79
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 3

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa


def test_data_QuattrePompeAttive_quando_LivelloEInRange_allora_NessunaDecisione():
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

    TOT POMPE                                                            4
    ATTIVE

    """

    livello_attuale = 79
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 4

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert not decisione_disattiva_pompa


def test_data_CinquePompeAttive_quando_LivelloEInRange_allora_DisattivaPompa():
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

    TOT POMPE                                                            5
    ATTIVE

    """

    livello_attuale = 79
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 5

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert not decisione_attiva_pompa
    assert decisione_disattiva_pompa



def test_data_UnaPompeAttive_quando_LivelloEInRange_allora_AttivaPompa_3():
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

    TOT POMPE                                                            1
    ATTIVE

    """

    livello_attuale = 79
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 1

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert decisione_attiva_pompa
    assert not decisione_disattiva_pompa




def test_data_ZeroPompeAttive_quando_LivelloEInRange_allora_AttivaPompa_3():
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

    TOT POMPE                                                            0
    ATTIVE

    """

    livello_attuale = 79
    soglie = [
        (60, 50),
        (70, 65),
        (80, 75),
        (90, 78)
    ]
    tot_pompe_attive_adesso = 0

    decisione_attiva_pompa, decisione_disattiva_pompa = decidi_se_attivare_o_disattivare_pompe(
        livello_attuale,
        soglie,
        tot_pompe_attive_adesso
    )

    assert decisione_attiva_pompa
    assert not decisione_disattiva_pompa