# # 1. Exemplo 1: condicionais simples
# def fiqueEmcasa():
#     print("Fique em casa e aproveite para relaxar!")


# def vaiBrincar():
#     print("O tempo está bom, vá brincar lá fora!")


# def vaiParaPiscina():
#     print("O tempo está bom, vá para a piscina!")


# estaChovendo = True

# if estaChovendo:
#     fiqueEmcasa()

# # 2. Exemplo 2: condicionais compostas
# estaChovendo = False

# if estaChovendo:
#     fiqueEmcasa()
# else:
#     vaiBrincar()

# # 3 Exemplo 3: condicionais com elif
# temSunga = True

# if estaChovendo:
#     fiqueEmcasa()
# elif temSunga:
#     vaiParaPiscina()
# else:
#     vaiBrincar()

# # 1. PRIMEIRO EXERCICIO DE CONDIÇOES
# x = 4
# y = 3

# if x == y:
#     print("x é igual a y")
# elif x < y:
#     print("x é menor que y")
# elif x > y:
#     print("x é maior que y")
# else:
#     print("x não é igual a y")


# condicoes.py


def determinar_acao_chuva(esta_chovendo: bool) -> str:
    """Determina a ação com base no clima."""
    if esta_chovendo:
        return "Fique em casa e aproveite para relaxar!"
    return "O tempo está bom, vá brincar lá fora!"


def determinar_acao_piscina(esta_chovendo: bool, tem_sunga: bool) -> str:
    """Determina a ação com base no clima e roupa."""
    if esta_chovendo:
        return "Fique em casa e aproveite para relaxar!"
    elif tem_sunga:
        return "O tempo está bom, vá para a piscina!"
    return "O tempo está bom, vá brincar lá fora!"


def comparar_numeros(x: int, y: int) -> str:
    """Compara dois números e retorna o resultado."""
    if x == y:
        return "x é igual a y"
    elif x < y:
        return "x é menor que y"
    return "x é maior que y"
