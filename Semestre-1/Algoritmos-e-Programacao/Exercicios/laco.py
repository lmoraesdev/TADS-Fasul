#  while estaChovendo:
#   espereEmCasa()
# vaiBrincar()

n = 0
#
"""
while n <= 5:
    print(n)
    n += 1
else:
    print("Numeros de 1 a 5 já Impressos")
"""


def imprime_numeros():
    numeros = list(range(6))
    mensagem = "Numeros de 1 a 5 já Impressos"
    print("\n".join(map(str, numeros)))
    print(mensagem)
    return numeros, mensagem
