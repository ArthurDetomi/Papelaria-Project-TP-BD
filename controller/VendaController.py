from persistence.VendaDao import VendaDao
from persistence.ItemDao import ItemDao
from persistence.ProdutoDao import ProdutoDao

from datetime import datetime

from model.Venda import Venda

class VendaController:
    def __init__(self):
        self.venda_dao = VendaDao()
        self.item_dao = ItemDao()
        self.produto_dao = ProdutoDao()

    def cadastrar_venda(self, venda : Venda) -> bool:
        id_venda = self.venda_dao.save(venda)

        if id_venda == None:
            return False

        venda.id = id_venda

        items = venda.items

        for item in items:
            self.item_dao.save(item)

            produto = item.produto
            produto.quantidade -= item.quantidade
            produto.editado = datetime.now()

            self.produto_dao.update_quantidade(produto)

        return True

    def find_all(self) -> list:
        return self.venda_dao.find_all()

    def delete(self, venda_id : int):
        # Deletar Items e dar update em estoque dos produtos
        items = self.item_dao.find_by_venda_id(venda_id=venda_id)

        for item in items:
            produto = item.produto
            produto.quantidade += item.quantidade
            produto.editado = datetime.now()

            self.produto_dao.update_quantidade(produto)
            self.item_dao.delete(venda_id=venda_id)

        return self.venda_dao.delete(venda_id)

