from controller.ClienteController import ClienteController
cliente_controller = ClienteController()

def exibir_menu_cliente():
    print("\n=== Menu Cliente ===")
    print("[0] Voltar")
    print("[1] Cadastrar Cliente")
    print("[2] Atualizar Cliente")
    print("[3] Deletar Cliente")
    print("[4] Listar Clientes")

    opcao = input("Escolha uma opção: ")
    return opcao

def view_cadastrar_cliente():
    print("\n=== Cadastrar Cliente ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")

    cliente_controller.cadastrar_cliente(nome=nome, cpf=cpf, telefone=telefone)


def view_atualizar_cliente():
    print("\n=== Atualizar Cliente ===")
    id = input("ID do cliente: ")
    nome = input("Novo Nome (deixe em branco para manter o atual): ")
    cpf = input("Novo CPF (deixe em branco para manter o atual): ")
    telefone = input("Novo Telefone (deixe em branco para manter o atual): ")

    cliente_controller.atualizar_cliente(id=id, nome=nome, cpf=cpf, telefone=telefone)


def view_deletar_cliente():
    print("\n=== Deletar Cliente ===")
    id = input("ID do cliente: ")

    cliente_controller.deletar_cliente(id)


def view_listar_cliente():
    print("\n=== Lista de Clientes ===")

    clientes = cliente_controller.listar_clientes()
    if clientes:
        for cliente in clientes:
                print(f"ID: {cliente.id}, Nome: {cliente.nome}, Telefone: {cliente.telefone}, CPF: {cliente.cpf}")
    else:
        print("Nenhum cliente cadastrado")
