import datetime

class Cliente:
    def __init__(self, id : int, nome : str, cpf : str, telefone : str, cadastrado : datetime, editado : datetime):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cadastrado = cadastrado
        self.editado = editado
        