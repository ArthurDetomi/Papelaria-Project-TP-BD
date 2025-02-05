from Venda import Venda
from Produto import Produto
import datetime

class Item:
    def __init__(self, id : int,venda : Venda, produto : Produto, quantidade : int, desconto : float, valor : float, cadastrado : datetime):
        self.id = id
        self.venda = venda
        self.produto = produto
        self.quantidade = quantidade
        self.desconto = desconto
        self.valor = valor
        self.cadastrado = cadastrado
        