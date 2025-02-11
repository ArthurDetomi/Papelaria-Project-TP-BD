
from model.Cliente import Cliente

from persistence.ClienteDao import ClienteDao

class ClienteController:
    def __init__(self):
        self.cliente_dao = ClienteDao()

    def buscar_por_cpf(self, cpf=""):
        return self.cliente_dao.find_by_cpf(cpf)

    def cadastrar_cliente(self, nome, cpf, telefone):
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone)
        if self.cliente_dao.save(cliente):
            print("Cliente cadastrado com sucesso!")
        else:
            print("Cliente já cadastrado!")

    def atualizar_cliente(self, id, nome, cpf, telefone):
        cliente = self.cliente_dao.find_by_id(id)

        if cliente:
            cliente.nome = nome or cliente.nome
            cliente.cpf = cpf or cliente.cpf
            cliente.telefone = telefone or cliente.telefone
            self.cliente_dao.update(cliente)
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def deletar_cliente(self, id):
        cliente = self.cliente_dao.find_by_id(id)
        if cliente:
            self.cliente_dao.delete(id)
            print("Cliente deletado com sucesso!")
        else:
            print("Cliente não encontrado.")

    def listar_clientes(self):
        clientes = self.cliente_dao.find_all()

        return clientes