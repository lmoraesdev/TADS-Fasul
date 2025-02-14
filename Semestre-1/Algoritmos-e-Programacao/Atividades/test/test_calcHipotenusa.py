from calcHipotenusa import calcHipotenusa


def test_calcHipotenusa():
    """Testa cálculos básicos da hipotenusa."""
    assert calcHipotenusa(3, 4) == 5.0
    assert calcHipotenusa(5, 12) == 13.0
    assert calcHipotenusa(8, 15) == 17.0
    assert calcHipotenusa(7, 24) == 25.0


def test_calcHipotenusa_decimais():
    """Testa cálculos com números decimais."""
    assert calcHipotenusa(2.5, 6) == 6.5
    assert calcHipotenusa(1.1, 2.2) == 2.46  # Considerando arredondamento


def test_calcHipotenusa_erros():
    """Testa valores inválidos que devem gerar erro."""
    for valores in [(-3, 4), (3, 0), (0, 0)]:
        try:
            calcHipotenusa(*valores)
            assert (
                False
            ), f"Erro esperado para valores {valores}, mas a função não falhou."
        except ValueError:
            pass  # Exceção esperada, o teste passa
