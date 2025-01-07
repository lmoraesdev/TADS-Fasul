# variavel = input("Digite um valor: ")

# nome = input("Digite seu nome: ")
# saudacao = "Olá, " + nome + "!"
# print(saudacao)

# PREVININDO ERROS

"""
Testa se de fato conseguimos converter o inout para int.
se der errado, entao, avisa o usuario.
se der certo, executa a conta.
"""
try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
except ValueError:
    print("Você deve inserir apenas números inteiros.")
else:
    print("A soma dos números é", num1 + num2)
