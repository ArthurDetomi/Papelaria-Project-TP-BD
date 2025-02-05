import datetime
from Usuario import Usuario
from Cliente import Cliente
from FormaPagamento import FormaPagamento

class Venda:
    def __init__(self, id : int, usuario : Usuario, cliente : Cliente, formaPagamento : FormaPagamento, total : float, cadastrado : datetime):
        self.id = id,
        self.usuario = usuario
        self.formaPagamento = formaPagamento
        self.cliente = cliente
        self.total = total
        self.cadastrado = cadastrado
        