from persistence.GenericDao import GenericDao
from persistence.Database import Database

from model.Produto import Produto

class ProdutoDao(GenericDao):

    def find_by_nome(self, nome) -> Produto:
        with Database() as db:
            result = db.query("SELECT * FROM produto WHERE nome = %s", params=(nome,), fetch_one=True)

        if result is None:
            return None

        id_, nome, preco, categoria, quantidade, unidadeMedida, cadastrado, editado = result

        return Produto(id=id_, nome=nome, preco=preco, categoria=categoria, quantidade=quantidade,
                       unidadeMedida=unidadeMedida, cadastrado=cadastrado, editado=editado)

    def update_quantidade(self, produto : Produto):
        with Database() as db:
            result = db.query("UPDATE produto SET quantidade = %s, editado = %s WHERE id = %s",
                (produto.quantidade, produto.editado,produto.id,))
        return result

