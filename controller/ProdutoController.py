"""Módulo ProdutoController.

Contém a classe ProdutoController, responsável por gerenciar as operações relacionadas
a produtos, como cadastro, atualização, busca e exclusão.
"""

from model.Produto import Produto
from persistence.ProdutoDao import ProdutoDao
from persistence.CategoriaDao import CategoriaDao


class ProdutoController:
    """Controlador para operações relacionadas a Produto."""

    def __init__(self):
        # Inicializa as instâncias de ProdutoDao e CategoriaDao para acesso aos dados.
        self.produto_dao = ProdutoDao()
        self.categoria_dao = CategoriaDao()

    def buscar_por_nome(self, nome_produto: str) -> Produto:
        """
        Busca um produto pelo nome.

        :param nome_produto: Nome do produto a ser buscado.
        :return: Produto encontrado ou None.
        """
        return self.produto_dao.find_by_nome(nome_produto)

    def cadastrar_produto(self, nome: str, preco: float, categoria: int,
                           quantidade: int, unidade_medida: str):
        """
        Cadastra um novo produto.

        :param nome: Nome do produto.
        :param preco: Preço do produto.
        :param categoria: ID da categoria do produto.
        :param quantidade: Quantidade disponível do produto.
        :param unidade_medida: Unidade de medida do produto.
        :return: Produto recém-cadastrado.
        """
        categoria_obj = self.categoria_dao.find_by_id(categoria)
        produto = Produto(
            nome=nome,
            preco=preco,
            categoria=categoria_obj,
            quantidade=quantidade,
            unidade_medida=unidade_medida
        )
        return self.produto_dao.save(produto=produto)

    def atualizar_produto(self, id: int, nome: str, preco: float, categoria: int,
                          quantidade: int, unidade_medida: str):
        """
        Atualiza os dados de um produto existente.

        :param id: ID do produto a ser atualizado.
        :param nome: Novo nome do produto.
        :param preco: Novo preço do produto.
        :param categoria: Novo ID da categoria do produto.
        :param quantidade: Nova quantidade disponível.
        :param unidade_medida: Nova unidade de medida.
        :return: Resultado da operação de atualização.
        """
        try:
            produto = self.produto_dao.find_by_id(id)
            if categoria:
                nova_categoria = self.categoria_dao.find_by_id(categoria)
                produto.categoria = nova_categoria
            if nome:
                produto.nome = nome
            if preco:
                produto.preco = preco
            if quantidade:
                produto.quantidade = quantidade
            if unidade_medida:
                produto.unidade_medida = unidade_medida
            self.produto_dao.update(produto)
        except ValueError:
            return ValueError

    def deletar(self, id):
        """
        Deleta um produto pelo seu ID.

        :param id: ID do produto a ser deletado.
        :return: Resultado da operação de exclusão.
        """
        return self.produto_dao.delete(id)

    def listar(self):
        """
        Lista todos os produtos cadastrados.

        :return: Lista de produtos.
        """
        return self.produto_dao.find_all()

    def find_by_id(self, id):
        """
        Busca um produto pelo seu ID.

        :param id: ID do produto.
        :return: Produto encontrado ou None.
        """
        return self.produto_dao.find_by_id(id)
