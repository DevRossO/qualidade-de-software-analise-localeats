def quantidade_itens_valida(quantidade):
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    return 1 <= quantidade <= 10
