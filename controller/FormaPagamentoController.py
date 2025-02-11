"""Módulo FormaPagamentoController.

Contém a classe FormaPagamentoController, que gerencia as operações relacionadas
às formas de pagamento (listar, cadastrar, atualizar e deletar).
"""

from model.FormaPagamento import FormaPagamento
from persistence.FormaPagamentoDao import FormaPagamentoDao


class FormaPagamentoController:
    """Controlador para operações relacionadas a Forma de Pagamento."""

    def __init__(self):
        # Inicializa a instância de FormaPagamentoDao para acesso aos dados.
        self.forma_pagamento_dao = FormaPagamentoDao()

    def find_all(self):
        """
        Retorna todas as formas de pagamento cadastradas.

        :return: Lista de formas de pagamento.
        """
        return self.forma_pagamento_dao.find_all()

    def cadastrar(self, nome: str):
        """
        Cria e salva uma nova forma de pagamento.

        :param nome: Nome da forma de pagamento.
        :return: Forma de pagamento recém-cadastrada.
        """
        forma_pagamento = FormaPagamento(nome=nome)
        return self.forma_pagamento_dao.save(forma_pagamento)

    def find_by_id(self, id):
        """
        Busca uma forma de pagamento pelo seu ID.

        :param id: ID da forma de pagamento.
        :return: Forma de pagamento encontrada ou None.
        """
        return self.forma_pagamento_dao.find_by_id(id)

    def atualizar(self, forma_pagamento: FormaPagamento):
        """
        Atualiza uma forma de pagamento existente.

        :param forma_pagamento: Objeto FormaPagamento com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        return self.forma_pagamento_dao.update(forma_pagamento)

    def deletar(self, id):
        """
        Deleta uma forma de pagamento pelo seu ID.

        :param id: ID da forma de pagamento a ser deletada.
        :return: Resultado da operação de exclusão.
        """
        return self.forma_pagamento_dao.delete(id)
