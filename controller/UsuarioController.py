"""Módulo UsuarioController.

Contém a classe UsuarioController, responsável por gerenciar as operações relacionadas
aos usuários, como login, cadastro, atualização e exclusão.
"""

from datetime import datetime
from model.Usuario import Usuario
from persistence.UsuarioDao import UsuarioDao
from service.UserSession import UserSession


class UsuarioController:
    """Controlador para operações relacionadas a Usuário."""

    def __init__(self):
        # Inicializa a instância de UsuarioDao para acesso aos dados do usuário.
        self.usuario_dao = UsuarioDao()

    def realizar_login(self, login: str, senha: str):
        """
        Realiza o login do usuário.

        :param login: Nome de usuário.
        :param senha: Senha do usuário.
        :return: True se o login for bem-sucedido, caso contrário, False.
        """
        logged_user = self.usuario_dao.find_by_login_and_senha(login, senha)
        if logged_user is None:
            return False
        UserSession.set_logged_user(logged_user)
        return True

    def cadastrar_usuario(self, login, senha, cpf):
        """
        Cadastra um novo usuário.

        :param login: Nome de usuário.
        :param senha: Senha do usuário.
        :param cpf: CPF do usuário.
        :return: Usuário recém-cadastrado.
        """
        usuario = Usuario(login=login, senha=senha, cpf=cpf)
        return self.usuario_dao.save(usuario)

    def atualizar_usuario(self, id, login, senha, cpf):
        """
        Atualiza os dados de um usuário existente.

        :param id: ID do usuário.
        :param login: Novo nome de usuário.
        :param senha: Nova senha.
        :param cpf: Novo CPF.
        :return: Resultado da operação de atualização.
        """
        usuario = Usuario(id=id, login=login, senha=senha, cpf=cpf)
        usuario.login = login or usuario.login
        usuario.senha = senha or usuario.senha
        usuario.cpf = cpf or usuario.cpf
        usuario.editado = datetime.now()
        return self.usuario_dao.update(usuario)

    def deletar_usuario(self, id):
        """
        Deleta um usuário pelo seu ID.

        :param id: ID do usuário a ser deletado.
        :return: Resultado da operação de exclusão.
        """
        return self.usuario_dao.delete(id)

    def find_by_id(self, id):
        """
        Busca um usuário pelo seu ID.

        :param id: ID do usuário.
        :return: Usuário encontrado ou None.
        """
        return self.usuario_dao.find_by_id(id)

    def listar_usuarios(self):
        """
        Lista todos os usuários cadastrados.

        :return: Lista de usuários.
        """
        return self.usuario_dao.find_all()
