"""Módulo FormaPagamentoDao.

Contém a classe FormaPagamentoDao, responsável pelas operações de acesso a dados
da entidade FormaPagamento no banco de dados.
"""

from persistence.Database import Database
from model.FormaPagamento import FormaPagamento


class FormaPagamentoDao:
    """DAO (Data Access Object) para a entidade FormaPagamento."""

    def find_all(self):
        """
        Recupera todas as formas de pagamento do banco de dados.

        :return: Lista de objetos FormaPagamento.
        """
        with Database() as db:
            result = db.query("SELECT * FROM forma_pagamento", fetch=True)

        forma_pagamentos = []
        for data in result:
            id_, nome, cadastrado, editado = data
            fp = FormaPagamento(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)
            forma_pagamentos.append(fp)

        return forma_pagamentos

    def find_by_id(self, id):
        """
        Recupera uma forma de pagamento com base no seu ID.

        :param id: ID da forma de pagamento.
        :return: Objeto FormaPagamento se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query(
                "SELECT * FROM forma_pagamento WHERE id = %s",
                params=(id,),
                fetch_one=True
            )

        if result is None:
            return None

        id_, nome, cadastrado, editado = result
        return FormaPagamento(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)

    def save(self, forma_pagamento: FormaPagamento):
        """
        Insere uma nova forma de pagamento no banco de dados.

        :param forma_pagamento: Objeto FormaPagamento a ser salvo.
        :return: Resultado da operação de inserção.
        """
        with Database() as db:
            result = db.query("INSERT INTO forma_pagamento (nome) VALUES (%s)", (forma_pagamento.nome,))
        return result

    def delete(self, id):
        """
        Remove uma forma de pagamento do banco de dados com base no seu ID.

        :param id: ID da forma de pagamento a ser removida.
        :return: Resultado da operação de exclusão.
        """
        with Database() as db:
            result = db.query("DELETE FROM forma_pagamento WHERE id = %s", (id,))
        return result

    def update(self, forma_pagamento: FormaPagamento):
        """
        Atualiza os dados de uma forma de pagamento existente.

        :param forma_pagamento: Objeto FormaPagamento com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            result = db.query(
                "UPDATE forma_pagamento SET nome=%s, editado=%s WHERE id = %s",
                (forma_pagamento.nome, forma_pagamento.editado, forma_pagamento.id,)
            )
        return result
