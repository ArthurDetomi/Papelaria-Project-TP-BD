from model.Produto import Produto

from persistence.ProdutoDao import ProdutoDao

class ProdutoController:
    def __init__(self):
        self.produto_dao = ProdutoDao()

    def buscar_por_nome(self, nome_produto : str) -> Produto:
        return self.produto_dao.find_by_nome(nome_produto)

