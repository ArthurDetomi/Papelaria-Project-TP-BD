from model.Produto import Produto
from model.Categoria import Categoria
from persistence.ProdutoDao import ProdutoDao
from persistence.CategoriaDao import CategoriaDao
from datetime import datetime

from persistence.ProdutoDao import ProdutoDao

class ProdutoController:
    def __init__(self):
        self.produto_dao = ProdutoDao()
        self.categoria_dao = CategoriaDao()

    def buscar_por_nome(self, nome_produto: str) -> Produto:
        return self.produto_dao.find_by_nome(nome_produto)

    def CadastrarProduto(self, nome: str, preco: float, categoria: int, quantidade: int, unidade_medida: str):
        categoria_obj = self.categoria_dao.find_by_id(categoria)
        produto = Produto(
            nome=nome,
            preco=preco,
            categoria=categoria_obj,
            quantidade=quantidade,
            unidadeMedida=unidade_medida
        )
        
        return self.produto_dao.save(produto=produto)

    def AtualizarProduto(self, id: int, nome: str, preco: float, categoria: int, quantidade: int, unidade_medida: str):

        try:
            id_produto = int(input("ID do produto: "))
            produto = self.produto_dao.find_by_id(id_produto)
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
                produto.unidadeMedida = unidade_medida
            self.produto_dao.update(produto)
                
        except ValueError:
            return ValueError

    def deletar(self, id):
        return self.produto_dao.delete(id)


    def listar(self):
        return self.produto_dao.find_all()

    def find_by_id(self, id):
        return self.produto_dao.find_by_id(id)
