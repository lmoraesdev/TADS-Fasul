from ..variaveis import verificar_tipo, converter_tipo


def test_verificar_tipo():
    assert verificar_tipo(7) == "<class 'int'>"
    assert verificar_tipo(3.14) == "<class 'float'>"
    assert verificar_tipo(True) == "<class 'bool'>"


def test_converter_tipo():
    assert converter_tipo("7", "int") == 7
    assert converter_tipo(7, "str") == "7"
    assert converter_tipo("True", "bool") is True
    assert converter_tipo(3.14, "int") == 3
