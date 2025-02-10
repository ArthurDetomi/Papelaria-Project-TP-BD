from model.Categoria import Categoria
from persistence.CategoriaDao import CategoriaDao
from datetime import datetime

class CategoriaController:
    def __init__(self):
        self.categoria = CategoriaDao()

    def __init__(self):
        self.categoria_dao = CategoriaDao()

    def find_all(self):
        return self.categoria_dao.find_all()

    def cadastrar(self, nome : str):
        categoria = Categoria(nome=nome)
    
        return self.categoria_dao.save(categoria)

    def find_by_id(self, id):
        return self.categoria_dao.find_by_id(id)

    def atualizar(self, forma_pagamento : Categoria):
        return self.categoria_dao.update(forma_pagamento)

    def deletar(self, id):
        return self.categoria_dao.delete(id)
