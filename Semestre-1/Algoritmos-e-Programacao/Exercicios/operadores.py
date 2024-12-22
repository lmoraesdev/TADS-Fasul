# OPERADORES UNARIOS
print("\n---------------------\nOPERADORES UNARIOS")

print("Operador '~' : ", ~10)
print("Operador '+' : ", +10)
print("Operador '-' : ", -10)

# OPERADORES ARITMÉTICOS
print("\n---------------------\nOPERADORES ARITMÉTICOS")
x = 10
y = 5

print("Operador '+' : ", x + y)
print("Operador '-' : ", x - y)
print("Operador '*' : ", x * y)
print("Operador '/' : ", x / y)
print("Operador '%' : ", x % y)
print("Operador '**' : ", x**y)
print("Operador '//' : ", x // y)

# OPERADORES RELACIONAIS
print("\n---------------------\nOPERADORES RELACIONAIS")
x = 10
y = 5

print("Operador '==' : ", x == y)
print("Operador '!=' : ", x != y)
print("Operador '>' : ", x > y)
print("Operador '<' : ", x < y)
print("Operador '>=' : ", x >= y)
print("Operador '<=' : ", x <= y)

# OPERADORES ARITMÉTICOS
print("\n---------------------\nOPERADORES LÓGICOS")
x = True
y = False

print("Operador 'and' : ", x and y)
print("Operador 'or' : ", x or y)
print("Operador 'and not' : ", x and not y)
print("Operador 'not' : ", not x)

# OPERADORES DE ATRIBUIÇÃO
print("\n---------------------\nOPERADORES DE ATRIBUIÇÃO")
x = 10
y = 5

x += y
print("Operador '+=' : ", x)

x -= y
print("Operador '-=' : ", x)

x *= y
print("Operador '*=' : ", x)

x /= y
print("Operador '/=' : ", x)

x %= y
print("Operador '%=' : ", x)

x **= y
print("Operador '**=' : ", x)

x //= y
print("Operador '//=' : ", x)

# PRECEDÊNCIA DE OPERADORES
print("\n---------------------\nPRECEDÊNCIA DE OPERADORES")

# 1. EXPOENTE E UNARIOS
print(-(2**2))
print(2**-2)

# 2. aritméticos. primeiro multiplicação e divisão, depois soma e subtração
print(1 + 3 / 3 * 1)

# 3. Depois de comparação, seguindo de igualde
print(False != 3 > 2)

# 4. Por fim, operadores lógicos
print(False != 3 > 2 and True)
