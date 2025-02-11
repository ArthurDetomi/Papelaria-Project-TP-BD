"""Módulo VendaDao.

Contém a classe VendaDao, responsável pelas operações de acesso a dados
da entidade Venda.
"""

from persistence.GenericDao import GenericDao
from model.Venda import Venda
from model.Cliente import Cliente
from model.Usuario import Usuario
from model.FormaPagamento import FormaPagamento
from persistence.Database import Database


class VendaDao(GenericDao):
    """DAO (Data Access Object) para a entidade Venda."""

    def find_all(self):
        """
        Recupera todas as vendas do banco de dados, incluindo informações do usuário,
        cliente e forma de pagamento.

        :return: Lista de objetos Venda.
        """
        query = (
            "SELECT v.*, u.login as login, c.nome as cliente_nome, fp.nome as fp_nome "
            "FROM venda as v "
            "INNER JOIN usuario as u ON v.usuario_id = u.id "
            "LEFT JOIN cliente as c ON v.cliente_id = c.id "
            "INNER JOIN forma_pagamento as fp ON v.forma_pagamento_id = fp.id"
        )

        vendas = []
        with Database() as db:
            result = db.query(query=query, fetch=True)

        for data in result:
            id_, usuario_id, cliente_id, forma_pagamento_id, total, cadastrado, login, nome_cliente, nome_fp = data

            usuario = Usuario(id=usuario_id, login=login)
            forma_pagamento = FormaPagamento(id=forma_pagamento_id, nome=nome_fp)
            cliente = Cliente(id=cliente_id, nome=nome_cliente)
            venda = Venda(
                id=id_,
                usuario=usuario,
                forma_pagamento=forma_pagamento,
                cliente=cliente,
                total=total,
                cadastrado=cadastrado
            )
            vendas.append(venda)

        return vendas

    def save(self, venda: Venda):
        """
        Insere uma nova venda no banco de dados e retorna o ID da venda inserida.

        :param venda: Objeto Venda a ser salvo.
        :return: ID da venda inserida se bem-sucedida, caso contrário None.
        """
        venda.preparar_entidade_para_cadastro()
        cliente_id = venda.cliente.id if venda.cliente else None

        with Database() as db:
            result = db.query(
                "INSERT INTO venda (usuario_id, cliente_id, forma_pagamento_id, total) VALUES (%s, %s, %s, %s)",
                (venda.usuario.id, cliente_id, venda.forma_pagamento.id, venda.total,)
            )

            result = db.query(
                "SELECT id FROM venda WHERE usuario_id = %s AND total = %s ORDER BY id DESC LIMIT 1",
                (venda.usuario.id, venda.total,),
                fetch=True
            )

        return result[0][0] if result else None

    def delete(self, id):
        """
        Remove uma venda do banco de dados com base no seu ID.

        :param id: ID da venda a ser removida.
        :return: Resultado da operação de exclusão.
        """
        with Database() as db:
            result = db.query("DELETE FROM venda WHERE id = %s", (id,))

        print(result)
        return result
