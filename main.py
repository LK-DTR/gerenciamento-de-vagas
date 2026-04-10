from data.vagas import lista_vagas
from modules.visualizar_vagas import exibir_vagas
from modules.atualizar_vagas import reservar_vaga
from modules.vagas_reservadas import listar_reservas

def menu() :

    print("\n--- SISTEMA DE RESERVA DE VAGAS ---")
    print("1. Visualizar Vagas Disponíveis")
    print("2. Reservar uma Vaga")
    print("3. Ver Relatório de Reservas")
    print("0. Sair")
    return input("Escolha uma opção: ")


def main():
    while True:
        opcao = menu()

        if opcao == "1":
            # Chama a função do módulo visualizar-vagas.py
            print("\nQUADRO DE VAGAS:")
            exibir_vagas(lista_vagas)

        elif opcao == "2":
            # Solicita o ID e usa a lógica do módulo atualizar-vagas.py
            id_vaga = int(input("Digite o ID da vaga que deseja reservar: "))
            sucesso = reservar_vaga(lista_vagas, id_vaga)
            if sucesso:
                print(f"Sucesso! Vaga {id_vaga} agora está reservada.")
            else:
                print("Erro: Vaga não encontrada ou já ocupada.")

        elif opcao == "3":
            # Chama a função do módulo vagas-reservadas.py
            print("\nRELATÓRIO DE OCUPAÇÃO:")
            listar_reservas(lista_vagas)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()