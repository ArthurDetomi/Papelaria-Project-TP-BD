from persistence.GenericDao import GenericDao
from persistence.Database import Database
from model.Item import Item

class ItemDao(GenericDao):

    def save(self, item : Item):
        with Database() as db:
            result = db.query("insert into item (venda_id, produto_id, quantidade, desconto, valor) values (%s, %s, %s, %s, %s);"
                , (item.venda.id, item.produto.id, item.quantidade, item.desconto, item.valor)
            )
        return result

    def delete(self, id):
        with Database() as db:
            result = db.query("DELETE FROM item WHERE id = %s", (id,))
        return result

