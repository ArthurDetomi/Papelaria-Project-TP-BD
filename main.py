from view.UsuarioView import exibir_menu
from controller.UsuarioController import UsuarioController
from controller.ClienteController import ClienteController

def main():
    usuario_controller = UsuarioController()
    cliente_controller = ClienteController()

    while True:
        opcao = exibir_menu()

        if opcao == "0":
            print("Saindo do sistema...")
            break
        elif opcao == "1":
            usuario_controller.cadastrar_usuario()
        elif opcao == "2":
            usuario_controller.atualizar_usuario()
        elif opcao == "3":
            usuario_controller.deletar_usuario()
        elif opcao == "4":
            usuario_controller.listar_usuarios()
        elif opcao == "5":
            cliente_controller.cadastrar_cliente()
        elif opcao == "6":
            cliente_controller.atualizar_cliente()
        elif opcao == "7":
            cliente_controller.deletar_cliente()
        elif opcao == "8":
            cliente_controller.listar_clientes()
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
