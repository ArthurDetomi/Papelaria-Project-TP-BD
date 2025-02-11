"""Módulo CategoriaDao.

Contém a classe CategoriaDao, responsável pelas operações de acesso a dados
da entidade Categoria no banco de dados.
"""

from persistence.Database import Database
from model.Categoria import Categoria


class CategoriaDao:
    """DAO (Data Access Object) para a entidade Categoria."""

    def find_all(self):
        """
        Recupera todas as categorias do banco de dados.

        :return: Lista de objetos Categoria.
        """
        with Database() as db:
            result = db.query("SELECT * FROM categoria", fetch=True)

        categorias = []
        for data in result:
            id_, nome, cadastrado, editado = data
            categoria = Categoria(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)
            categorias.append(categoria)

        return categorias

    def find_by_id(self, id):
        """
        Recupera uma categoria com base no seu ID.

        :param id: ID da categoria.
        :return: Objeto Categoria se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query("SELECT * FROM categoria WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cadastrado, editado = result
        return Categoria(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)

    def save(self, categoria: Categoria):
        """
        Insere uma nova categoria no banco de dados.

        :param categoria: Objeto Categoria a ser salvo.
        :return: Resultado da operação de inserção.
        """
        with Database() as db:
            result = db.query("INSERT INTO categoria (nome) VALUES (%s)", (categoria.nome,))
        return result

    def delete(self, id):
        """
        Remove uma categoria do banco de dados com base no seu ID.

        :param id: ID da categoria a ser removida.
        :return: Resultado da operação de exclusão.
        """
        with Database() as db:
            result = db.query("DELETE FROM categoria WHERE id = %s", (id,))
        return result

    def update(self, categoria: Categoria):
        """
        Atualiza os dados de uma categoria existente.

        :param categoria: Objeto Categoria com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            result = db.query(
                "UPDATE categoria SET nome=%s, editado=%s WHERE id = %s",
                (categoria.nome, categoria.editado, categoria.id,)
            )
        return result
