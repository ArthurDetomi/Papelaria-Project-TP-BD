import datetime
from Categoria import Categoria


class Produto:
    def __init__(self, id : int, nome : str, preco : float, categoria : Categoria, quantidade : int, unidadeMedida : str, cadastrado : datetime, editado : datetime):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade
        self.unidadeMedida = unidadeMedida
        self.cadastrado = cadastrado
        self.editado = editado