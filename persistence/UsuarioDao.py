"""Módulo UsuarioDao.

Contém a classe UsuarioDao, responsável pelas operações de acesso a dados
da entidade Usuario.
"""

from persistence.Database import Database
from model.Usuario import Usuario
from persistence.GenericDao import GenericDao


class UsuarioDao(GenericDao):
    """DAO (Data Access Object) para a entidade Usuario."""

    def find_all(self):
        """
        Recupera todos os usuários do banco de dados.

        :return: Lista de objetos Usuario.
        """
        with Database() as db:
            result = db.query("SELECT * FROM usuario", fetch=True)

        users = []
        for data in result:
            id_, login, senha, cpf, cadastrado, editado = data
            user = Usuario(
                id=id_,
                login=login,
                senha=senha,
                cpf=cpf,
                cadastrado=cadastrado,
                editado=editado
            )
            users.append(user)
        return users

    def find_by_id(self, id):
        """
        Recupera um usuário com base no seu ID.

        :param id: ID do usuário.
        :return: Objeto Usuario se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query("SELECT * FROM usuario WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, login, senha, cpf, cadastrado, editado = result
        return Usuario(
            id=id_,
            login=login,
            senha=senha,
            cpf=cpf,
            cadastrado=cadastrado,
            editado=editado
        )

    def find_by_login_and_senha(self, login: str, senha: str):
        """
        Recupera um usuário com base no login e na senha.

        :param login: Nome de login do usuário.
        :param senha: Senha do usuário.
        :return: Objeto Usuario se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query(
                "SELECT * FROM usuario WHERE login = %s AND senha = %s",
                params=(login, senha,),
                fetch_one=True
            )

        if result is None:
            return None

        id_, login, senha, cpf, cadastrado, editado = result
        return Usuario(
            id=id_,
            login=login,
            senha=senha,
            cpf=cpf,
            cadastrado=cadastrado,
            editado=editado
        )

    def save(self, usuario: Usuario):
        """
        Insere um novo usuário no banco de dados.

        :param usuario: Objeto Usuario a ser salvo.
        :return: Resultado da operação de inserção.
        """
        with Database() as db:
            result = db.query(
                "INSERT INTO usuario (login, senha, cpf) VALUES (%s, %s, %s)",
                (usuario.login, usuario.senha, usuario.cpf,)
            )
        return result

    def delete(self, id):
        """
        Remove um usuário do banco de dados com base no seu ID.

        :param id: ID do usuário a ser removido.
        :return: Resultado da operação de exclusão.
        """
        with Database() as db:
            result = db.query("DELETE FROM usuario WHERE id = %s", (id,))
        return result

    def update(self, usuario: Usuario):
        """
        Atualiza os dados de um usuário existente.

        :param usuario: Objeto Usuario com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            result = db.query(
                "UPDATE usuario SET login=%s, senha=%s, cpf=%s, editado=%s WHERE id = %s",
                (usuario.login, usuario.senha, usuario.cpf, usuario.editado, usuario.id,)
            )
        return result
