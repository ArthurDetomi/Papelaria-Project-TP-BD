from decimal import Decimal

class Item:
    def __init__(self, venda=None, produto=None, quantidade=None, desconto=None, valor=None, cadastrado=None):
        self.venda = venda
        self.produto = produto
        self.quantidade = quantidade
        self.desconto = desconto
        self.cadastrado = cadastrado
        self.valor = self.calcularValor()

    def calcularValor(self):
        if self.produto.preco is None or self.quantidade is None:
            return None

        valor_total = self.produto.preco * self.quantidade

        valor_com_desconto = Decimal(valor_total) * (Decimal('1') - Decimal(self.desconto) / Decimal('100'))

        return valor_com_desconto
