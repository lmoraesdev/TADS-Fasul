from ..outPut import output_print


def test_output_print():
    actual_result = output_print("Leandro", "Moraes", 8.323)
    expected_result = [
        "Nome: Leandro Moraes",
        "Idade: 8",
        "Idade: 8.323000",
        "Idade: 8.3",
    ]
    assert actual_result == expected_result
