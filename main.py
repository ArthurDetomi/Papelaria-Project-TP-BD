from view.UsuarioView import *
from view.ClienteView import *

def main():
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("[0] Sair do sistema")
        print("[1] Usuários")
        print("[2] Clientes")

        opcao_externa = int(input("Escolha uma opção: "))

        if opcao_externa == 1:
            while True:
                opcao_usuario = exibir_menu_usuario()

                if opcao_usuario == "0":
                    print("Voltando...")
                    break
                elif opcao_usuario == "1":
                    view_cadastrar_usuario()
                elif opcao_usuario == "2":
                    view_atualizar_usuario()
                elif opcao_usuario == "3":
                    view_deletar_usuario()
                elif opcao_usuario == "4":
                    view_listar_usuario()
                else:
                    print("Opção inválida, tente novamente.")
        elif opcao_externa == 2:
            while True:
                opcao_cliente = exibir_menu_cliente()

                if opcao_cliente == "0":
                    print("Voltando...")
                    break
                elif opcao_cliente == "1":
                    view_cadastrar_cliente()
                    print("Voltou do cadastro cliente")
                elif opcao_cliente == "2":
                    view_atualizar_cliente()
                elif opcao_cliente == "3":
                    view_deletar_cliente()
                elif opcao_cliente == "4":
                    view_listar_cliente()
                else:
                    print("Opção inválida, tente novamente.")
        else:
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()
