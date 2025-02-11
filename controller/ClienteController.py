
from model.Cliente import Cliente

from persistence.ClienteDao import ClienteDao

class ClienteController:
    def __init__(self):
        self.cliente_dao = ClienteDao()

    def buscar_por_cpf(self, cpf=""):
        return self.cliente_dao.find_by_cpf(cpf)

    def cadastrar_cliente(self, nome, cpf, telefone):
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone)
        return self.cliente_dao.save(cliente)

    def atualizar_cliente(self, id, nome, cpf, telefone):
        cliente = Cliente(id=id, nome=nome, cpf=cpf, telefone=telefone)
        
        cliente.nome = nome or cliente.nome
        cliente.cpf = cpf or cliente.cpf
        cliente.telefone = telefone or cliente.telefone
        
        return self.cliente_dao.update(cliente)


    def deletar(self, id):
        return self.cliente_dao.delete(id)
            
    def find_by_id(self, id):
        return self.cliente_dao.find_by_id(id)

    def listar(self):
        return self.cliente_dao.find_all()