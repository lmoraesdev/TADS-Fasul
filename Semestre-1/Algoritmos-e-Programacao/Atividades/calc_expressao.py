def calcular_expressao(a: int, b: int, c: int, d: bool, e: bool) -> bool:
    """
    Avalia a expressão lógica: a > 1000 and b < c and d or e
    """
    return (a > 1000 and b < c and d) or e
