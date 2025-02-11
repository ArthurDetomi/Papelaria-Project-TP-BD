"""Módulo Item.

Contém a classe Item que representa um item em uma venda, contendo informações
como produto, quantidade, desconto e valor calculado.
"""

from decimal import Decimal


class Item:
    """Classe que representa um Item em uma venda.

    Atributos:
        venda: Referência à venda associada ao item.
        produto: Produto associado ao item.
        quantidade: Quantidade do produto vendido.
        desconto: Desconto aplicado (em porcentagem).
        cadastrado: Data/hora de cadastro do item.
        valor: Valor calculado do item após desconto.
    """

    def __init__(self, venda=None, produto=None, quantidade=None, desconto=None, valor=None, cadastrado=None):
        """
        Inicializa uma nova instância de Item.

        :param venda: Referência à venda.
        :param produto: Produto associado.
        :param quantidade: Quantidade do produto.
        :param desconto: Desconto aplicado (em porcentagem).
        :param valor: Valor do item (opcional, será calculado).
        :param cadastrado: Data/hora de cadastro.
        """
        self.venda = venda
        self.produto = produto
        self.quantidade = quantidade
        self.desconto = desconto
        self.cadastrado = cadastrado
        self.valor = self.calcular_valor()

    def calcular_valor(self):
        """
        Calcula o valor do item aplicando o desconto.

        :return: Valor com desconto aplicado ou None se o preço do produto ou a quantidade não forem informados.
        """
        if self.produto.preco is None or self.quantidade is None:
            return None

        valor_total = self.produto.preco * self.quantidade
        valor_com_desconto = Decimal(valor_total) * (Decimal("1") - Decimal(self.desconto) / Decimal("100"))
        return valor_com_desconto
