def listar_reservas(lista_vagas):
    total_vagas = len(lista_vagas)
    ocupadas = 0
    livres = 0

    print("\n=== VAGAS OCUPADAS ===")

    for vaga in lista_vagas:
        if vaga["status"] == "ocupada":
            ocupadas += 1
            print(
                f"ID: {vaga['id']} | "
                f"Tipo: {vaga['tipo']} | "
                f"Setor: {vaga['setor']} | "
                f"Preço: R$ {vaga['preco']:.2f}"
            )
        else:
            livres += 1

    if ocupadas == 0:
        print("Nenhuma vaga ocupada no momento.")

    print("\n=== RESUMO ===")
    print(f"Total de vagas: {total_vagas}")
    print(f"Vagas ocupadas: {ocupadas}")
    print(f"Vagas livres: {livres}")