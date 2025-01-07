from ..condicoesLogica import verificar_aprovacao_dict


def test_verificar_aprovacao_reprovado_por_nota():
    resultado = verificar_aprovacao_dict(50, 80)
    assert resultado["status"] == "Reprovado"
    assert "nota baixa" in resultado["motivo"]


def test_verificar_aprovacao_reprovado_por_frequencia():
    resultado = verificar_aprovacao_dict(80, 50)
    assert resultado["status"] == "Reprovado"
    assert "frequência insuficiente" in resultado["motivo"]


def test_verificar_aprovacao_aprovado():
    resultado = verificar_aprovacao_dict(80, 80)
    assert resultado["status"] == "Aprovado"
    assert not resultado["motivo"]


def test_verificar_aprovacao_aprovado_com_louvor():
    resultado = verificar_aprovacao_dict(100, 100)
    assert resultado["status"] == "Aprovado com louvor"
    assert not resultado["motivo"]
