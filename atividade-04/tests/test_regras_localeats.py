from src.regras_localeats import quantidade_itens_valida

def test_quantidade_de_itens_dentro_do_limite_e_valida():
    resultado = quantidade_itens_valida(3)

    assert resultado is True

def test_quantidade_acima_do_limite_nao_e_valida():
    resultado = quantidade_itens_valida(11)

    assert resultado is False
