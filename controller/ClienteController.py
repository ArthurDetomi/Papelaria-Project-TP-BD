from model.Cliente import Cliente
from persistence.ClienteDao import ClienteDao

class ClienteController:
    def __init__(self):
        self.cliente_dao = ClienteDao()

    def cadastrar_cliente(self):
        print("\n=== Cadastrar Cliente ===")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")

        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone)
        self.cliente_dao.save(cliente)
        print("Cliente cadastrado com sucesso!")

    def atualizar_cliente(self):
        print("\n=== Atualizar Cliente ===")
        id = input("ID do cliente: ")
        cliente = self.cliente_dao.find_by_id(id)

        if cliente:
            print(f"Cliente encontrado: {cliente.nome} - {cliente.cpf}")
            nome = input("Novo Nome (deixe em branco para manter o atual): ") or cliente.nome
            cpf = input("Novo CPF (deixe em branco para manter o atual): ") or cliente.cpf
            telefone = input("Novo Telefone (deixe em branco para manter o atual): ") or cliente.telefone

            cliente.nome = nome
            cliente.cpf = cpf
            cliente.telefone = telefone
            self.cliente_dao.update(cliente)
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def deletar_cliente(self):
        print("\n=== Deletar Cliente ===")
        id = input("ID do cliente: ")

        cliente = self.cliente_dao.find_by_id(id)
        if cliente:
            self.cliente_dao.delete(id)
            print("Cliente deletado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def listar_clientes(self):
        print("\n=== Lista de Clientes ===")
        clientes = self.cliente_dao.find_all()

        if clientes:
            for cliente in clientes:
                print(f"ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}, Telefone: {cliente.telefone}")
        else:
            print("Nenhum cliente cadastrado.")
