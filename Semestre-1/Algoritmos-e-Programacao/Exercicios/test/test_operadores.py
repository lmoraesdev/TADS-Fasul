from ..operadores import (
    operadores_unarios,
    operadores_aritmeticos,
    operadores_relacionais,
    operadores_logicos,
)


def test_operadores_unarios():
    resultado = operadores_unarios(10)
    assert resultado["~"] == -11
    assert resultado["+"] == 10
    assert resultado["-"] == -10


def test_operadores_aritmeticos():
    resultado = operadores_aritmeticos(10, 5)
    assert resultado["+"] == 15
    assert resultado["-"] == 5
    assert resultado["*"] == 50
    assert resultado["/"] == 2.0


def test_operadores_relacionais():
    resultado = operadores_relacionais(10, 5)
    assert resultado["=="] is False
    assert resultado[">"] is True


def test_operadores_logicos():
    resultado = operadores_logicos(True, False)
    assert resultado["and"] is False
    assert resultado["or"] is True
