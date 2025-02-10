from persistence.GenericDao import GenericDao

from model.Venda import Venda
from model.Cliente import Cliente
from model.Usuario import Usuario
from model.FormaPagamento import FormaPagamento

from persistence.Database import Database

class VendaDao(GenericDao):

    def find_all(self):
        query = f"""select v.*, u.login as login, c.nome as cliente_nome, fp.nome as fp_nome
            from venda as v
            inner join usuario as u on v.usuario_id = u.id
            left join cliente as c on v.cliente_id = c.id
            inner join forma_pagamento as fp on v.forma_pagamento_id = fp.id"""

        vendas = []

        with Database() as db:
            result = db.query(query=query, fetch=True)

        for data in result:
            id_, usuario_id, cliente_id, forma_pagamento_id, total, cadastrado, login, nome_cliente, nome_fp = data

            usuario = Usuario(id=usuario_id, login=login)
            forma_pagamento = FormaPagamento(id=forma_pagamento_id, nome=nome_fp)
            cliente = Cliente(id=cliente_id, nome=nome_cliente)

            venda = Venda(id=id_, usuario=usuario,
                    forma_pagamento=forma_pagamento, cliente=cliente, total=total, cadastrado=cadastrado)

            vendas.append(venda)

        return vendas

    def save(self, venda : Venda):
        venda.prepararEntidadeParaCadastro()

        cliente_id = venda.cliente.id if venda.cliente else None

        with Database() as db:
            result = db.query("insert into venda (usuario_id, cliente_id, forma_pagamento_id, total) values (%s, %s, %s, %s)"
                , (venda.usuario.id, cliente_id, venda.forma_pagamento.id, venda.total,)
            )

            result = db.query("SELECT id FROM venda WHERE usuario_id = %s AND total = %s ORDER BY id DESC LIMIT 1",
                (venda.usuario.id, venda.total,), fetch=True)

        return result[0][0] if result else None

    def delete(self, id):
        with Database() as db:
            result = db.query("DELETE FROM venda WHERE id = %s", (id,))

        print(result)
        return result

