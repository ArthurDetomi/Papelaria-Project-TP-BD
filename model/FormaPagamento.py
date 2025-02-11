"""Módulo FormaPagamento.

Contém a classe FormaPagamento que representa uma forma de pagamento utilizada em uma venda.
"""

from termcolor import colored


class FormaPagamento:
    """Classe que representa uma Forma de Pagamento.

    Atributos:
        id: Identificador único da forma de pagamento.
        nome: Nome da forma de pagamento.
        cadastrado: Data/hora de cadastro.
        editado: Data/hora da última edição.
    """

    def __init__(self, id=None, nome=None, cadastrado=None, editado=None):
        """
        Inicializa uma nova instância de FormaPagamento.

        :param id: Identificador único da forma de pagamento.
        :param nome: Nome da forma de pagamento.
        :param cadastrado: Data/hora de cadastro.
        :param editado: Data/hora da última edição.
        """
        self.id = id
        self.nome = nome
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        """
        Retorna uma representação em string formatada da Forma de Pagamento.

        :return: Representação em string da forma de pagamento com cores.
        """
        return (
            f"{colored('ID:', 'cyan')} {self.id} | "
            f"{colored('Nome:', 'yellow')} {self.nome} | "
            f"{colored('Cadastrado:', 'green')} "
            f"{self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
            f"{colored('Editado:', 'blue')} "
            f"{self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )
