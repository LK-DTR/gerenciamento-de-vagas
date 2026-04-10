# modules/atualizar-vagas.py

from data.vagas import lista_vagas


def buscar_vaga_por_id(vaga_id):
    """Retorna a vaga com o ID informado."""
    for vaga in lista_vagas:
        if vaga["id"] == vaga_id:
            return vaga
    return None


def atualizar_status_vaga(vaga_id, novo_status):
    """
    Atualiza o status de uma vaga.
    novo_status deve ser 'livre' ou 'ocupada'
    """
    vaga = buscar_vaga_por_id(vaga_id)

    if vaga is None:
        return f"Vaga com ID {vaga_id} não encontrada."

    if novo_status not in ["livre", "ocupada"]:
        return "Status inválido. Use 'livre' ou 'ocupada'."

    vaga["status"] = novo_status
    return f"Vaga {vaga_id} atualizada para '{novo_status}'."


def listar_vagas(status=None, setor=None, tipo=None):
    """
    Lista vagas com filtros opcionais.
    """
    vagas_filtradas = lista_vagas

    if status:
        vagas_filtradas = [v for v in vagas_filtradas if v["status"] == status]

    if setor:
        vagas_filtradas = [v for v in vagas_filtradas if v["setor"] == setor]

    if tipo:
        vagas_filtradas = [v for v in vagas_filtradas if v["tipo"] == tipo]

    return vagas_filtradas


def ocupar_vaga(vaga_id):
    """Marca uma vaga como ocupada."""
    return atualizar_status_vaga(vaga_id, "ocupada")


def reservar_vaga(lista_vagas, id_vaga):
    """
    Tenta reservar uma vaga pelo ID.
    
    Retorna:
        True  -> se a reserva foi feita com sucesso
        False -> se a vaga não existe ou já está ocupada
    """
    
    for vaga in lista_vagas:
        if vaga["id"] == id_vaga:
            
            # Verifica se já está ocupada
            if vaga["status"] == "ocupada":
                return False
            
            # Atualiza status para ocupada
            vaga["status"] = "ocupada"
            return True

    # Caso não encontre a vaga
    return False


# Exemplo de uso (teste rápido)
if __name__ == "__main__":
    print(ocupar_vaga(1))
    print(reservar_vaga(2))
    print(listar_vagas(status="livre"))