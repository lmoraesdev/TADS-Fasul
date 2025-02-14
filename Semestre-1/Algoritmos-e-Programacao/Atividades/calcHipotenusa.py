import math


def calcular_hipotenusa(a: float, b: float) -> float:
    """Calcula a hipotenusa do triângulo retângulo dados os catetos a e b."""
    if a <= 0 or b <= 0:
        raise ValueError("Os valores dos catetos devem ser positivos.")

    return math.hypot(a, b)


if __name__ == "__main__":
    try:
        a = float(input("Digite o valor do cateto a: "))
        b = float(input("Digite o valor do cateto b: "))
        print(f"\nHipotenusa: {calcular_hipotenusa(a, b):.2f}")
    except ValueError:
        print("Por favor, insira um número válido.")
