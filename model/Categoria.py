"""Módulo Categoria.

Contém a classe Categoria que representa a categoria de um produto ou item.
"""

from termcolor import colored


class Categoria:
    """Classe que representa uma Categoria.

    Atributos:
        id: Identificador único da categoria.
        nome: Nome da categoria.
        cadastrado: Data/hora de cadastro.
        editado: Data/hora da última edição.
    """

    def __init__(self, id=None, nome="", cadastrado=None, editado=None):
        """
        Inicializa uma nova instância de Categoria.

        :param id: Identificador único da categoria.
        :param nome: Nome da categoria.
        :param cadastrado: Data/hora de cadastro.
        :param editado: Data/hora da última edição.
        """
        self.id = id
        self.nome = nome
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        """
        Retorna uma representação em string formatada da Categoria.

        :return: Representação em string da categoria com cores.
        """
        return (
            f"{colored('ID:', 'cyan')} {self.id} | "
            f"{colored('Nome:', 'yellow')} {self.nome} | "
            f"{colored('Cadastrado:', 'green')} "
            f"{self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
            f"{colored('Editado:', 'blue')} "
            f"{self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )
