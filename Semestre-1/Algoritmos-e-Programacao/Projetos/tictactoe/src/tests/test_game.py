from ..game import (
    novoTabuleiro,
    posicaoValida,
    mudarJogador,
    verificarFimDeJogo,
)


# Teste para novoTabuleiro
def test_novoTabuleiro():
    esperado = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert novoTabuleiro() == esperado


# Teste para posicaoValida
def test_posicaoValida():
    tabuleiro = [0, 1, 0, 2, 0, 0, 0, 0, 0]
    assert posicaoValida(1, tabuleiro) is True  # Válido
    assert posicaoValida(2, tabuleiro) is False  # Ocupado
    assert posicaoValida(10, tabuleiro) is False  # Fora do intervalo
    assert posicaoValida(0, tabuleiro) is False  # Fora do intervalo


# Teste para mudarJogador
def test_mudarJogador():
    tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    jogador_atual = "X"
    jogador_atual = mudarJogador(jogador_atual, 1, tabuleiro)
    assert jogador_atual == "O"
    assert tabuleiro[0] == 1

    jogador_atual = mudarJogador(jogador_atual, 2, tabuleiro)
    assert jogador_atual == "X"
    assert tabuleiro[1] == 2


# Teste para verificarFimDeJogo
def test_verificarFimDeJogo():
    tabuleiro = [1, 1, 1, 0, 0, 0, 0, 0, 0]  # Linha superior X
    assert verificarFimDeJogo(3, tabuleiro) == 1

    tabuleiro = [0, 0, 0, 2, 2, 2, 0, 0, 0]  # Linha do meio O
    assert verificarFimDeJogo(6, tabuleiro) == 1

    tabuleiro = [0, 0, 0, 0, 0, 0, 1, 1, 1]  # Linha inferior X
    assert verificarFimDeJogo(9, tabuleiro) == 1

    tabuleiro = [1, 0, 0, 1, 0, 0, 1, 0, 0]  # Coluna da esquerda X
    assert verificarFimDeJogo(7, tabuleiro) == 1

    tabuleiro = [0, 0, 2, 0, 0, 2, 0, 0, 2]  # Coluna da direita O
    assert verificarFimDeJogo(9, tabuleiro) == 1

    tabuleiro = [1, 0, 0, 0, 1, 0, 0, 0, 1]  # Diagonal X
    assert verificarFimDeJogo(9, tabuleiro) == 1

    tabuleiro = [0, 0, 2, 0, 2, 0, 2, 0, 0]  # Diagonal O
    assert verificarFimDeJogo(7, tabuleiro) == 1

    tabuleiro = [1, 2, 1, 2, 1, 2, 2, 1, 2]  # Deu velha
    assert verificarFimDeJogo(9, tabuleiro) == -1
