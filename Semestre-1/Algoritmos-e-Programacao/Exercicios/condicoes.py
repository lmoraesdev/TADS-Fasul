# 1. Exemplo 1: condicionais simples
def fiqueEmcasa():
    print("Fique em casa e aproveite para relaxar!")


def vaiBrincar():
    print("O tempo está bom, vá brincar lá fora!")


def vaiParaPiscina():
    print("O tempo está bom, vá para a piscina!")


estaChovendo = True

if estaChovendo:
    fiqueEmcasa()

# 2. Exemplo 2: condicionais compostas
estaChovendo = False

if estaChovendo:
    fiqueEmcasa()
else:
    vaiBrincar()

# 3 Exemplo 3: condicionais com elif
temSunga = True

if estaChovendo:
    fiqueEmcasa()
elif temSunga:
    vaiParaPiscina()
else:
    vaiBrincar()

# 1. PRIMEIRO EXERCICIO DE CONDIÇOES
x = 4
y = 3

if x == y:
    print("x é igual a y")
elif x < y:
    print("x é menor que y")
elif x > y:
    print("x é maior que y")
else:
    print("x não é igual a y")
