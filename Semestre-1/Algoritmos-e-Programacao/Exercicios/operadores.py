# # OPERADORES UNÁRIOS
# print("\n---------------------\nOPERADORES UNÁRIOS")
# print("Operador '~' : ", ~10)
# print("Operador '+' : ", +10)
# print("Operador '-' : ", -10)

# # OPERADORES ARITMÉTICOS
# print("\n---------------------\nOPERADORES ARITMÉTICOS")
# x = 10
# y = 5

# print("Operador '+' : ", x + y)
# print("Operador '-' : ", x - y)
# print("Operador '*' : ", x * y)
# print("Operador '/' : ", x / y)
# print("Operador '%' : ", x % y)
# print("Operador '**' : ", x**y)
# print("Operador '//' : ", x // y)

# # OPERADORES RELACIONAIS
# print("\n---------------------\nOPERADORES RELACIONAIS")
# print("Operador '==' : ", x == y)
# print("Operador '!=' : ", x != y)
# print("Operador '>' : ", x > y)
# print("Operador '<' : ", x < y)
# print("Operador '>=' : ", x >= y)
# print("Operador '<=' : ", x <= y)

# # OPERADORES LÓGICOS
# print("\n---------------------\nOPERADORES LÓGICOS")
# a = True
# b = False

# print("Operador 'and' : ", a and b)
# print("Operador 'or' : ", a or b)
# print("Operador 'and not' : ", a and not b)
# print("Operador 'not' : ", not a)

# # OPERADORES DE ATRIBUIÇÃO
# print("\n---------------------\nOPERADORES DE ATRIBUIÇÃO")
# x = 10
# y = 5

# x += y
# print("Operador '+=' : ", x)

# x -= y
# print("Operador '-=' : ", x)

# x *= y
# print("Operador '*=' : ", x)

# x /= y
# print("Operador '/=' : ", x)

# x %= y
# print("Operador '%=' : ", x)

# x **= y
# print("Operador '**=' : ", x)

# x //= y
# print("Operador '//=' : ", x)

# # PRECEDÊNCIA DE OPERADORES
# print("\n---------------------\nPRECEDÊNCIA DE OPERADORES")

# # 1. EXPOENTE E UNÁRIOS
# print("-(2**2) : ", -(2**2))
# print("2**-2 : ", 2**-2)

# # 2. Aritméticos: multiplicação e divisão têm precedência
# # sobre soma e subtração

# print("1 + 3 / 3 * 1 : ", 1 + 3 / 3 * 1)

# # 3. Comparação seguida de igualdade
# print("False != 3 > 2 : ", False != (3 > 2))

# # 4. Por fim, operadores lógicos
# print("False != 3 > 2 and True : ", (False != (3 > 2)) and True)

# operadores.py


def operadores_unarios(valor: int) -> dict:
    return {"~": ~valor, "+": +valor, "-": -valor}


def operadores_aritmeticos(x: int, y: int) -> dict:
    return {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y,
        "%": x % y,
        "**": x**y,
        "//": x // y,
    }


def operadores_relacionais(x: int, y: int) -> dict:
    return {
        "==": x == y,
        "!=": x != y,
        ">": x > y,
        "<": x < y,
        ">=": x >= y,
        "<=": x <= y,
    }


def operadores_logicos(a: bool, b: bool) -> dict:
    return {
        "and": a and b,
        "or": a or b,
        "not_a": not a,
        "a_and_not_b": a and not b,
    }
