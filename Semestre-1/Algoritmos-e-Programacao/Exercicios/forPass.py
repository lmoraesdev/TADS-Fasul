# for numero in range(5, 11):
#     if numero == 7:
#         pass
#     print("Numero com pass: ", numero)


# for numero in range(5, 11):
#     if numero == 7:
#         break
#     print("Numero com break: ", numero)

for numero in range(5, 11):
    if numero == 7:
        continue
    print("Numero com Continue: ", numero)


# forPass.py


def loop_with_pass():
    result = []
    for numero in range(5, 11):
        if numero == 7:
            pass
        result.append(f"Numero com pass: {numero}")
    return result


def loop_with_break():
    result = []
    for numero in range(5, 11):
        if numero == 7:
            break
        result.append(f"Numero com break: {numero}")
    return result


def loop_with_continue():
    result = []
    for numero in range(5, 11):
        if numero == 7:
            continue
        result.append(f"Numero com continue: {numero}")
    return result
