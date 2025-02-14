from ..calc_expressao import calcular_expressao


def test_calcular_expressao():
    """Testa a expressão com os valores fornecidos na tabela."""
    assert calcular_expressao(1500, 50, 100, True, False) == True
    assert calcular_expressao(500, 20, 21, True, True) == True
    assert calcular_expressao(2000, 30, 10, False, False) == False
