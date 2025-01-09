from src.game import (
    novoTabuleiro,
    ImprimirTabuleiro,
    recebeJogada,
    posicaoValida,
    mudarJogador,
    verificarFimDeJogo,
)

tabuleiro = novoTabuleiro()

jogador = "X"
jogadas = 0


while True:
    ImprimirTabuleiro(tabuleiro)
    jogada = recebeJogada(jogador)
    if not posicaoValida(jogada, tabuleiro):
        continue
    jogador = mudarJogador(jogador, jogada, tabuleiro)
    jogadas += 1
    if verificarFimDeJogo(jogadas, tabuleiro) != 0:
        break
