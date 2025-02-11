"""Módulo VendaController.

Contém a classe VendaController, responsável por gerenciar as operações relacionadas
a vendas, incluindo cadastro, listagem e exclusão, com atualização dos estoques.
"""

from datetime import datetime
from model.Venda import Venda
from persistence.VendaDao import VendaDao
from persistence.ItemDao import ItemDao
from persistence.ProdutoDao import ProdutoDao


class VendaController:
    """Controlador para operações relacionadas a Venda."""

    def __init__(self):
        # Inicializa as instâncias de VendaDao, ItemDao e ProdutoDao para acesso aos dados.
        self.venda_dao = VendaDao()
        self.item_dao = ItemDao()
        self.produto_dao = ProdutoDao()

    def cadastrar_venda(self, venda: Venda) -> bool:
        """
        Cadastra uma nova venda e atualiza a quantidade dos produtos vendidos.

        :param venda: Objeto Venda contendo os detalhes da venda e os itens.
        :return: True se a venda for cadastrada com sucesso, False caso contrário.
        """
        id_venda = self.venda_dao.save(venda)
        if id_venda is None:
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
        """
        Lista todas as vendas cadastradas.

        :return: Lista de vendas.
        """
        return self.venda_dao.find_all()

    def delete(self, venda_id: int):
        """
        Deleta uma venda e reverte as alterações na quantidade dos produtos vendidos.

        :param venda_id: ID da venda a ser deletada.
        :return: Resultado da operação de exclusão.
        """
        items = self.item_dao.find_by_venda_id(venda_id=venda_id)

        for item in items:
            produto = item.produto
            produto.quantidade += item.quantidade
            produto.editado = datetime.now()
            self.produto_dao.update_quantidade(produto)
            self.item_dao.delete(venda_id=venda_id)

        return self.venda_dao.delete(venda_id)
