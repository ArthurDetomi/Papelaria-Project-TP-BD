"""Módulo UserSession.

Contém a classe UserSession para gerenciar a sessão do usuário logado.
"""

from model.Usuario import Usuario


class UserSession:
    """Classe para gerenciar a sessão do usuário logado.

    Essa classe armazena o usuário atualmente logado de forma global.
    """
    logged_user = None

    @classmethod
    def set_logged_user(cls, usuario: Usuario):
        """
        Define o usuário logado na sessão.

        :param usuario: Instância de Usuario a ser definida como logado.
        """
        cls.logged_user = usuario

    @classmethod
    def get_logged_user(cls) -> Usuario:
        """
        Retorna o usuário atualmente logado na sessão.

        :return: Instância de Usuario logado ou None se nenhum usuário estiver logado.
        """
        return cls.logged_user
