"""Módulo CategoriaController.

Contém a classe CategoriaController, responsável por gerenciar as operações de
categoria (listar, cadastrar, atualizar e deletar).
"""

from model.Categoria import Categoria
from persistence.CategoriaDao import CategoriaDao


class CategoriaController:
    """Controlador para operações relacionadas a Categoria."""

    def __init__(self):
        # Inicializa a instância de CategoriaDao para acesso aos dados de categoria.
        self.categoria_dao = CategoriaDao()

    def find_all(self):
        """
        Retorna todas as categorias cadastradas.

        :return: Lista de categorias.
        """
        return self.categoria_dao.find_all()

    def cadastrar(self, nome: str):
        """
        Cria e salva uma nova categoria.

        :param nome: Nome da nova categoria.
        :return: Categoria recém-cadastrada.
        """
        categoria = Categoria(nome=nome)
        return self.categoria_dao.save(categoria)

    def find_by_id(self, id):
        """
        Busca uma categoria pelo seu ID.

        :param id: ID da categoria.
        :return: Categoria encontrada ou None.
        """
        return self.categoria_dao.find_by_id(id)

    def atualizar(self, categoria: Categoria):
        """
        Atualiza os dados de uma categoria existente.

        :param categoria: Objeto Categoria com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        return self.categoria_dao.update(categoria)

    def deletar(self, id):
        """
        Deleta uma categoria pelo seu ID.

        :param id: ID da categoria a ser deletada.
        :return: Resultado da operação de exclusão.
        """
        return self.categoria_dao.delete(id)
