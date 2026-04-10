# modules/visualizar_vagas.py

def exibir_vagas(lista_vagas):
    if not lista_vagas:
        print("Atenção: Não há vagas cadastradas no sistema.")
        return

    print("\n--- LISTA DE VAGAS ---")
    for vaga in lista_vagas:
        # Usamos o print para garantir que apareça no console
        print(f"ID: {vaga['id']} | Setor: {vaga['setor']} | Status: {vaga['status']}")