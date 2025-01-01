# nota = 80
# presenca = 70

# if nota < 70 or presenca < 70:
#     print("Você foi reprovado.")

#     if nota < 70:
#         print("Tente melhorar sua nota ano que vem.")
#     if presenca < 70:
#         print("Você deve frequentar mais as aulas.")

# else:
#     print("Você passou de ano!")

#     if nota == 100 and presenca == 100:
#         print("Aprovado com louvor!")


def verificar_aprovacao_dict(nota, presenca):
    """
    Retorna os resultados da função verificar_aprovacao em um formato de dicionário.
    """
    if nota < 70 or presenca < 70:
        motivo = []
        if nota < 70:
            motivo.append("nota baixa")
        if presenca < 70:
            motivo.append("frequência insuficiente")
        return {"status": "Reprovado", "motivo": motivo}
    else:
        status = "Aprovado"
        if nota == 100 and presenca == 100:
            status = "Aprovado com louvor"
        return {"status": status, "motivo": []}
