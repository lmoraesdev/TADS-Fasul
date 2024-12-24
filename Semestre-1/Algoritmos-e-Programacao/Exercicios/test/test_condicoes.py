# test_condicoes.py

from ..condicoes import determinar_acao_chuva, determinar_acao_piscina, comparar_numeros


def test_determinar_acao_chuva():
    assert determinar_acao_chuva(True) == "Fique em casa e aproveite para relaxar!"
    assert determinar_acao_chuva(False) == "O tempo está bom, vá brincar lá fora!"


def test_determinar_acao_piscina():
    assert (
        determinar_acao_piscina(True, True) == "Fique em casa e aproveite para relaxar!"
    )
    assert (
        determinar_acao_piscina(False, True) == "O tempo está bom, vá para a piscina!"
    )
    assert (
        determinar_acao_piscina(False, False) == "O tempo está bom, vá brincar lá fora!"
    )


def test_comparar_numeros():
    assert comparar_numeros(4, 4) == "x é igual a y"
    assert comparar_numeros(3, 4) == "x é menor que y"
    assert comparar_numeros(5, 4) == "x é maior que y"
