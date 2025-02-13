from ..calcSalario import calcula_novo_salario


def test_calcula_novo_salario():
    # Teste para aumento de 10% sobre 1000, deve resultar em 1100.0
    assert calcula_novo_salario(1000, 10) == 1100.0


def test_sem_aumento():
    # Teste para aumento de 0% deve retornar o mesmo salário
    assert calcula_novo_salario(1500, 0) == 1500.0


def test_aumento_negativo():
    # Teste para redução (aumento negativo): -10% de 1000 deve resultar em 900.0
    assert calcula_novo_salario(1000, -10) == 900.0


def test_aumento_fracionado():
    # Teste para aumento fracionado: 12.5% de 800 deve resultar em 900.0
    resultado = calcula_novo_salario(800, 12.5)
    assert abs(resultado - 900.0) < 1e-6
