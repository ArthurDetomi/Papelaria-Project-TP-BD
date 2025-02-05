import datetime

class Categoria:
    def __init__(self, id : int, nome : str, cadastrado : datetime, editado : datetime):
        self.id = id
        self.nome = nome
        self.cadastrado = cadastrado
        self.editado = editado
        