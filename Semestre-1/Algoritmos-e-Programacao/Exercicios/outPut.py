# arquivo = open("arquivo.txt", "w")
# print("print no arquivo", file=arquivo)
# arquivo.close()

nome = "Leandro"
sobreNome = "Moraes"

print("Nome", nome + " " + sobreNome, sep=": ", end="\n")

# Formatar Variáveis
idade = 8.323
print("Idade: %d" % idade)
print("Idade: %f" % idade)
print("Idade: %.1f" % idade)


def output_print(nome, sobreNome, idade):
    result = [
        f"Nome: {nome} {sobreNome}",
        f"Idade: {int(idade)}",  # Inteiro
        f"Idade: {idade:.6f}",  # 6 casas decimais
        f"Idade: {idade:.1f}",  # 1 casa decimal
    ]
    for line in result:  # Imprime cada linha
        print(line)
    return result
