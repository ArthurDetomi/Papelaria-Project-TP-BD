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

    def buscar_por_nome(self, nome_produto : str) -> Produto:
        return self.produto_dao.find_by_nome(nome_produto)

    def save(self, produto : Produto):
        return self.produto_dao.save(produto)
        

    def update(self, produto : Produto):
        return self.produto_dao.update(produto=produto)
        

    def deletar(self, id):
        return self.produto_dao.delete(id)


    def listar(self):
        return self.produto_dao.find_all()

    def find_by_id(self, id):
        return self.produto_dao.find_by_id(id)
