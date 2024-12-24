from ..condicoes import determinar_acao_chuva, determinar_acao_piscina, comparar_numeros


def test_determinar_acao_chuva():
    resultado = determinar_acao_chuva(True)
    assert resultado == "Fique em casa e aproveite para relaxar!"

    resultado = determinar_acao_chuva(False)
    assert resultado == "O tempo está bom, vá brincar lá fora!"


def test_determinar_acao_piscina():
    resultado = determinar_acao_piscina(True, True)
    assert resultado == "Fique em casa e aproveite para relaxar!"

    resultado = determinar_acao_piscina(False, True)
    assert resultado == "O tempo está bom, vá para a piscina!"

    resultado = determinar_acao_piscina(False, False)
    assert resultado == "O tempo está bom, vá brincar lá fora!"


def test_comparar_numeros():
    resultado = comparar_numeros(4, 4)
    assert resultado == "x é igual a y"

    resultado = comparar_numeros(3, 4)
    assert resultado == "x é menor que y"

    resultado = comparar_numeros(5, 4)
    assert resultado == "x é maior que y"
