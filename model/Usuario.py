"""Módulo Usuario.

Contém a classe Usuario que representa um usuário do sistema.
"""

from termcolor import colored


class Usuario:
    """Classe que representa um Usuário.

    Atributos:
        id: Identificador único do usuário.
        login: Nome de login do usuário.
        senha: Senha do usuário.
        cpf: CPF do usuário.
        cadastrado: Data/hora de cadastro.
        editado: Data/hora da última edição.
    """

    def __init__(self, id=None, login="", senha="", cpf="", cadastrado=None, editado=None):
        """
        Inicializa uma nova instância de Usuario.

        :param id: Identificador único do usuário.
        :param login: Nome de login do usuário.
        :param senha: Senha do usuário.
        :param cpf: CPF do usuário.
        :param cadastrado: Data/hora de cadastro.
        :param editado: Data/hora da última edição.
        """
        self.id = id
        self.login = login
        self.senha = senha
        self.cpf = cpf
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        """
        Retorna uma representação em string formatada do Usuário.

        :return: Representação em string do usuário com cores.
        """
        return (
            f"{colored('ID:', 'cyan')} {self.id} | "
            f"{colored('Login:', 'yellow')} {self.login} | "
            f"{colored('CPF:', 'green')} {self.cpf} | "
            f"{colored('Cadastrado:', 'blue')} "
            f"{self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
            f"{colored('Editado:', 'magenta')} "
            f"{self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )
