"""Módulo ItemDao.

Contém a classe ItemDao, responsável pelas operações de acesso a dados da entidade Item.
"""

from persistence.GenericDao import GenericDao
from persistence.Database import Database
from model.Item import Item
from model.Produto import Produto


class ItemDao(GenericDao):
    """DAO (Data Access Object) para a entidade Item."""

    def save(self, item: Item):
        """
        Insere um novo item no banco de dados.

        :param item: Objeto Item a ser salvo.
        :return: Resultado da operação de inserção.
        """
        with Database() as db:
            result = db.query(
                "INSERT INTO item (venda_id, produto_id, quantidade, desconto, valor) VALUES (%s, %s, %s, %s, %s);",
                (item.venda.id, item.produto.id, item.quantidade, item.desconto, item.valor)
            )
        return result

    def delete(self, venda_id: int):
        """
        Remove itens associados a uma venda específica.

        :param venda_id: ID da venda cujos itens serão removidos.
        :return: Resultado da operação de exclusão.
        """
        with Database() as db:
            result = db.query("DELETE FROM item WHERE venda_id = %s", (venda_id,))
        return result

    def find_by_venda_id(self, venda_id):
        """
        Recupera os itens associados a uma venda com base no ID da venda.

        :param venda_id: ID da venda.
        :return: Lista de objetos Item.
        """
        with Database() as db:
            result = db.query(
                """
                SELECT i.produto_id as p_id, p.quantidade as p_qtd, i.quantidade as i_qtd
                FROM item AS i
                INNER JOIN produto AS p ON i.produto_id = p.id
                WHERE venda_id = %s
                """,
                params=(venda_id,),
                fetch=True
            )

        items = []
        for data in result:
            p_id, p_qtd, i_qtd = data
            produto = Produto(id=p_id, quantidade=p_qtd)
            items.append(Item(produto=produto, quantidade=i_qtd))
        return items
