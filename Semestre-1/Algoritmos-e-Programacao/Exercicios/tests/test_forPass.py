from ..forPass import loop_with_pass, loop_with_break, loop_with_continue


def test_loop_with_pass():
    # Testa se a função loop_with_pass retorna o resultado esperado
    result = loop_with_pass()
    expected_result = [
        "Numero com pass: 5",
        "Numero com pass: 6",
        "Numero com pass: 7",  # 'pass' não afeta, 7 é incluído
        "Numero com pass: 8",
        "Numero com pass: 9",
        "Numero com pass: 10",
    ]
    assert result == expected_result


def test_loop_with_break():
    # Testa se a função loop_with_break retorna o resultado esperado
    result = loop_with_break()
    expected_result = [
        "Numero com break: 5",
        "Numero com break: 6",
    ]  # Quando chega no 7, o loop é interrompido
    assert result == expected_result


def test_loop_with_continue():
    # Testa se a função loop_with_continue retorna o resultado esperado
    result = loop_with_continue()
    expected_result = [
        "Numero com continue: 5",
        "Numero com continue: 6",
        "Numero com continue: 8",
        "Numero com continue: 9",
        "Numero com continue: 10",
    ]  # Quando chega no 7, ele é ignorado e o loop continua
    assert result == expected_result
