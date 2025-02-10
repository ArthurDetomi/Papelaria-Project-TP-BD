from persistence.ClienteDao import ClienteDao

class ClienteController:
    def __init__(self):
        self.cliente_dao = ClienteDao()

    def buscar_por_cpf(self, cpf=""):
        return self.cliente_dao.find_by_cpf(cpf)
