from ..laco import imprime_numeros


def test_imprime_numeros():
    # Chamar a função que retorna os números e a mensagem
    numeros, mensagem = imprime_numeros()

    # Verificar se os números estão corretos
    assert numeros == [0, 1, 2, 3, 4, 5]

    # Verificar se a mensagem está correta
    assert mensagem == "Numeros de 1 a 5 já Impressos"
