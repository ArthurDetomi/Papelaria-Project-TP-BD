from persistence.GenericDao import GenericDao
from persistence.Database import Database

from model.Item import Item
from model.Produto import Produto

class ItemDao(GenericDao):

    def save(self, item : Item):
        with Database() as db:
            result = db.query("insert into item (venda_id, produto_id, quantidade, desconto, valor) values (%s, %s, %s, %s, %s);"
                , (item.venda.id, item.produto.id, item.quantidade, item.desconto, item.valor)
            )
        return result

    def delete(self, venda_id : int):
        with Database() as db:
            result = db.query("DELETE FROM item WHERE venda_id = %s", (venda_id,))
        return result

    def find_by_venda_id(self, venda_id):
        with Database() as db:
            result = db.query("""
                select i.produto_id as p_id, p.quantidade as p_qtd, i.quantidade as i_qtd from item as i inner join produto as p on i.produto_id = p.id where venda_id = %s
            """, params=(venda_id,), fetch=True)

        items = []

        for data in result:
            p_id, p_qtd, i_qtd = data

            produto = Produto(id=p_id, quantidade=p_qtd)
            items.append(Item(produto=produto, quantidade=i_qtd))

        return items
