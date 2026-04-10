"""Funcoes de atualizacao e reserva de vagas."""


def buscar_vaga_por_id(lista_vagas, id_vaga):
    """Retorna o dicionario da vaga com o ID informado."""
    for vaga in lista_vagas:
        if vaga["id"] == id_vaga:
            return vaga
    return None


def atualizar_status_vaga(lista_vagas, id_vaga, novo_status):
    """Atualiza o status para 'livre' ou 'ocupada'."""
    if novo_status not in ["livre", "ocupada"]:
        return False

    vaga = buscar_vaga_por_id(lista_vagas, id_vaga)
    if vaga is None:
        return False

    if vaga["status"] == novo_status:
        return False

    vaga["status"] = novo_status
    return True


def reservar_vaga(lista_vagas, id_vaga):
    """Reserva uma vaga livre pelo ID."""
    return atualizar_status_vaga(lista_vagas, id_vaga, "ocupada")


def liberar_vaga(lista_vagas, id_vaga):
    """Libera uma vaga ocupada pelo ID."""
    return atualizar_status_vaga(lista_vagas, id_vaga, "livre")