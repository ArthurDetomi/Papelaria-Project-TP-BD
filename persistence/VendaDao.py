from persistence.GenericDao import GenericDao
from model.Venda import Venda
from persistence.Database import Database

class VendaDao(GenericDao):

    def save(self, venda : Venda):
        with Database() as db:
            result = db.query("insert into venda (usuario_id, cliente_id, forma_pagamento_id, total) values (%s, %s, %s, %s);"
                , (venda.usuario.id, venda.cliente.id, venda.formaPagamento.id, venda.total)
            )
        return result

    def delete(self, id):
        with Database() as db:
            result = db.query("DELETE FROM venda WHERE id = %s", (id,))
        return result

