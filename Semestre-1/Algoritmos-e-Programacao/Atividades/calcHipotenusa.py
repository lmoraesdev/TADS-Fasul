import math


def calcular_hipotenusa():
    try:
        a = float(input("Digite o valor do cateto a: "))
        b = float(input("Digite o valor do cateto b: "))

        if a <= 0 or b <= 0:
            print("Os valores dos catetos devem ser positivos.")
            return

        c = math.hypot(a, b)  # Usa math.hypot() para melhor precisão
        print(f"\nCateto a: {a:.2f}\nCateto b: {b:.2f}\nHipotenusa: {c:.2f}")

    except ValueError:
        print("Por favor, insira um número válido.")


if __name__ == "__main__":
    calcular_hipotenusa()
