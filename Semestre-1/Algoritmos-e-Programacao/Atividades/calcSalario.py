def calcula_novo_salario(salario, porcentagem):
    """
    Calcula o novo salário com base no salário atual e na porcentagem de aumento.
    """
    aumento = salario * (porcentagem / 100)
    novo_salario = salario + aumento
    return novo_salario


if __name__ == "__main__":
    try:
        salario = float(input("Digite o salário do funcionário: "))
        porcentagem = float(input("Digite a porcentagem de aumento: "))
        novo_salario = calcula_novo_salario(salario, porcentagem)
        print("Novo salário: R$ {:.2f}".format(novo_salario))
    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")
