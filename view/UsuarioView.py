from controller.UsuarioController import UsuarioController
usuario_controller = UsuarioController()

def exibir_menu_usuario():
    print("\n=== Menu Usuario ===")
    print("[0] Voltar")
    print("[1] Cadastrar Usuário")
    print("[2] Atualizar Usuário")
    print("[3] Deletar Usuário")
    print("[4] Listar Usuários")

    opcao = input("Escolha uma opção: ")
    return opcao

def view_cadastrar_usuario():
    print("\n=== Preencha as credenciais ===")
    login = input("Login: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")

    usuario_controller.cadastrar_usuario(login=login, senha=senha, cpf=cpf)


def view_atualizar_usuario():
    print("\n=== Atualizar Usuário ===")
    id = int(input("ID do usuário: "))
    login = input("Novo Login (deixe em branco para manter o atual): ")
    senha = input("Nova Senha (deixe em branco para manter a atual): ")
    cpf = input("Novo CPF (deixe em branco para manter o atual): ")

    usuario_controller.atualizar_usuario(id=id, login=login, senha=senha, cpf=cpf)


def view_deletar_usuario():
    print("\n=== Deletar Usuário ===")
    id = input("ID do usuário: ")

    usuario_controller.deletar_usuario(id)


def view_listar_usuario():
    print("\n=== Lista de Usuários ===")    
    
    usuarios = usuario_controller.listar_usuarios()
    if usuarios:
        for usuario in usuarios:
                print(f"ID: {usuario.id}, Login: {usuario.login}, CPF: {usuario.cpf}")
    else:
        print("Nenhum usuario cadastrado")
