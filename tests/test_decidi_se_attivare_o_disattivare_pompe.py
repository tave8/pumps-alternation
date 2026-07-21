from src.main import decidi_se_attivare_o_disattivare_pompe


def test_data_ZeroPompeAttive_quando_LivelloEIlPiuBasso_allora_NonCiSonoDecisioniDaPrendere():
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

