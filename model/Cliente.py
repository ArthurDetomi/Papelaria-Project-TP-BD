"""Módulo Cliente.

Contém a classe Cliente que representa um cliente com seus dados pessoais.
"""

from termcolor import colored


class Cliente:
    """Classe que representa um Cliente.

    Atributos:
        id: Identificador único do cliente.
        nome: Nome do cliente.
        cpf: CPF do cliente.
        telefone: Telefone do cliente.
        cadastrado: Data/hora de cadastro.
        editado: Data/hora da última edição.
    """

    def __init__(self, id=None, nome="", cpf="", telefone=None, cadastrado=None, editado=None):
        """
        Inicializa uma nova instância de Cliente.

        :param id: Identificador único do cliente.
        :param nome: Nome do cliente.
        :param cpf: CPF do cliente.
        :param telefone: Telefone do cliente.
        :param cadastrado: Data/hora de cadastro.
        :param editado: Data/hora da última edição.
        """
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        """
        Retorna uma representação em string formatada do Cliente.

        :return: Representação em string do cliente com cores.
        """
        return (
            f"{colored('ID:', 'cyan')} {self.id} | "
            f"{colored('Nome:', 'yellow')} {self.nome} | "
            f"{colored('CPF:', 'green')} {self.cpf} | "
            f"{colored('Telefone:', 'blue')} "
            f"{self.telefone if self.telefone else 'Não informado'} | "
            f"{colored('Cadastrado:', 'magenta')} "
            f"{self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
            f"{colored('Editado:', 'red')} "
            f"{self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )
