class Item:
    def __init__(self, id=None,venda=None, produto=None, quantidade=None, desconto=None, valor=None, cadastrado=None):
        self.id = id
        self.venda = venda
        self.produto = produto
        self.quantidade = quantidade
        self.desconto = desconto
        self.cadastrado = cadastrado
        self.valor = self.calcularValor()

    def calcularValor(self):
        valor_total = self.produto.preco * self.quantidade

        valor_com_desconto = valor_total * (1 - self.desconto / 100)

        return valor_com_desconto
