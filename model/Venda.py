"""Módulo Venda.

Contém a classe Venda que representa uma venda realizada no sistema.
"""

from termcolor import colored


class Venda:
    """Classe que representa uma Venda.

    Atributos:
        id: Identificador único da venda.
        usuario: Usuário que realizou a venda.
        items: Lista de itens vendidos.
        cliente: Cliente associado à venda.
        forma_pagamento: Forma de pagamento utilizada.
        total: Valor total da venda.
        cadastrado: Data/hora do cadastro da venda.
    """

    def __init__(self, id=None, usuario=None, items=None, cliente=None,
                 forma_pagamento=None, total=None, cadastrado=None):
        """
        Inicializa uma nova instância de Venda.

        :param id: Identificador único da venda.
        :param usuario: Usuário que realizou a venda.
        :param items: Lista de itens vendidos.
        :param cliente: Cliente associado à venda.
        :param forma_pagamento: Forma de pagamento utilizada.
        :param total: Valor total da venda.
        :param cadastrado: Data/hora do cadastro da venda.
        """
        self.id = id
        self.usuario = usuario
        self.forma_pagamento = forma_pagamento
        self.cliente = cliente
        self.total = total
        self.cadastrado = cadastrado
        self.items = items if items is not None else []

    def preparar_entidade_para_cadastro(self):
        """
        Calcula e prepara o valor total da venda somando os valores dos itens.

        Atualiza o atributo total da venda.
        """
        valor_total = 0
        for item in self.items:
            valor_total += item.valor
        self.total = valor_total

    def __str__(self):
        """
        Retorna uma representação em string formatada da Venda.

        :return: Representação em string da venda com cores.
        """
        return (
            f"{colored('ID Venda:', 'cyan')} {self.id} | "
            f"{colored('Usuario:', 'yellow')} {self.usuario.login} | "
            f"{colored('Cliente:', 'green')} "
            f"{self.cliente.nome if self.cliente else 'Não informado'} | "
            f"{colored('Forma Pagamento:', 'blue')} "
            f"{self.forma_pagamento.nome if self.forma_pagamento else 'Não informado'} | "
            f"{colored('Total:', 'magenta')} {self.total if self.total else 'Não calculado'} | "
            f"{colored('Cadastrado:', 'green')} "
            f"{self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
        )
