from calcHipotenusa import calcular_hipotenusa


def test_calcHipotenusa():
    """Testa cálculos básicos da hipotenusa."""
    assert calcular_hipotenusa(3, 4) == 5.0
    assert calcular_hipotenusa(5, 12) == 13.0
    assert calcular_hipotenusa(8, 15) == 17.0
    assert calcular_hipotenusa(7, 24) == 25.0


def test_calcHipotenusa_decimais():
    """Testa cálculos com números decimais."""
    assert calcular_hipotenusa(2.5, 6) == 6.5
    assert calcular_hipotenusa(1.1, 2.2) == 2.46  # Considerando arredondamento


def test_calcHipotenusa_erros():
    """Testa valores inválidos que devem gerar erro."""
    for valores in [(-3, 4), (3, 0), (0, 0)]:
        try:
            calcular_hipotenusa(*valores)
            assert (
                False
            ), f"Erro esperado para valores {valores}, mas a função não falhou."
        except ValueError:
            pass  # Exceção esperada, o teste passa
