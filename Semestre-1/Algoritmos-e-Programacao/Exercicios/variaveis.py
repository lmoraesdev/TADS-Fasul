# print("\n---------------------\nDECLARANDO VARIÁVEIS")
# x = 7

# # TIPO INTEIRO
# print("\n---------------------\nTIPO INTEIRO")
# print(x)
# print(type(x))

# # TIPO FLOAT
# print("\n---------------------\nTIPO FLOAT")
# ponto_flutuante = 3.14
# print(ponto_flutuante)
# print(type(ponto_flutuante))

# # TIPO BOOL
# print("\n---------------------\nTIPO BOOL")
# booleano_true = True
# booleanoFalse = False
# print(booleano_true)
# print(type(booleano_true))
# print(booleanoFalse)
# print(type(booleanoFalse))

# # TIPO STRING
# print("\n---------------------\nTIPO STRING")
# string = "Helloworld"
# print(string)
# print(type(string))

# # Conversão entre tipos
# print("\n---------------------\nCONVERSÃO ENTRE TIPOS")

# # INT -> FLOAT
# print("\n---------------------\nINT -> FLOAT")
# x = 7
# print(x)
# print(type(x))
# x = float(x)
# print(x)
# print(type(x))

# # FLOAT -> INT
# print("\n---------------------\nFLOAT -> INT")
# x = 3.14
# print(x)
# print(type(x))
# x = int(x)
# print(x)
# print(type(x))

# # STRING -> INT
# print("\n---------------------\nSTRING -> INT")
# x = "7"
# print(x)
# print(type(x))
# x = int(x)
# print(x)
# print(type(x))

# # STRING -> FLOAT
# print("\n---------------------\nSTRING -> FLOAT")
# x = "3.14"
# print(x)
# print(type(x))
# x = float(x)
# print(x)
# print(type(x))

# # STRING -> BOOL
# print("\n---------------------\nSTRING -> BOOL")
# x = "True"
# print(x)
# print(type(x))
# x = bool(x)
# print(x)
# print(type(x))

# # BOOL -> INT
# print("\n---------------------\nBOOL -> INT")
# x = True
# print(x)
# print(type(x))
# x = int(x)
# print(x)
# print(type(x))

# # BOOL -> FLOAT
# print("\n---------------------\nBOOL -> FLOAT")
# x = False
# print(x)
# print(type(x))
# x = float(x)
# print(x)
# print(type(x))

# # BOOL -> STRING
# print("\n---------------------\nBOOL -> STRING")
# x = True
# print(x)
# print(type(x))
# x = str(x)
# print(x)
# print(type(x))

# # INT -> STRING
# print("\n---------------------\nINT -> STRING")
# x = 7
# print(x)
# print(type(x))
# x = str(x)
# print(x)
# print(type(x))

# # FLOAT -> STRING
# print("\n---------------------\nFLOAT -> STRING")
# x = 3.14
# print(x)
# print(type(x))
# x = str(x)
# print(x)
# print(type(x))


# variaveis.py


def verificar_tipo(valor) -> str:
    """Retorna o tipo de uma variável."""
    return str(type(valor))


def converter_tipo(valor, tipo: str):
    """Converte um valor para o tipo especificado."""
    if tipo == "int":
        return int(valor)
    elif tipo == "float":
        return float(valor)
    elif tipo == "str":
        return str(valor)
    elif tipo == "bool":
        return bool(valor)
    else:
        raise ValueError("Tipo não suportado")
