"""Módulo ClienteController.

Contém a classe ClienteController, responsável por gerenciar as operações relacionadas
ao cliente (busca, cadastro, atualização, exclusão e listagem).
"""

from model.Cliente import Cliente
from persistence.ClienteDao import ClienteDao


class ClienteController:
    """Controlador para operações relacionadas a Cliente."""

    def __init__(self):
        # Inicializa a instância de ClienteDao para acesso aos dados do cliente.
        self.cliente_dao = ClienteDao()

    def buscar_por_cpf(self, cpf=""):
        """
        Busca um cliente pelo CPF.

        :param cpf: CPF do cliente.
        :return: Cliente encontrado ou None.
        """
        return self.cliente_dao.find_by_cpf(cpf)

    def cadastrar_cliente(self, nome, cpf, telefone):
        """
        Cria e cadastra um novo cliente.

        :param nome: Nome do cliente.
        :param cpf: CPF do cliente.
        :param telefone: Telefone do cliente.
        :return: Cliente recém-cadastrado.
        """
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone)
        return self.cliente_dao.save(cliente)

    def atualizar_cliente(self, id, nome, cpf, telefone):
        """
        Atualiza os dados de um cliente existente.

        :param id: ID do cliente.
        :param nome: Novo nome do cliente.
        :param cpf: Novo CPF do cliente.
        :param telefone: Novo telefone do cliente.
        :return: Resultado da operação de atualização.
        """
        cliente = Cliente(id=id, nome=nome, cpf=cpf, telefone=telefone)
        # Atualiza os atributos somente se os novos valores forem fornecidos.
        cliente.nome = nome or cliente.nome
        cliente.cpf = cpf or cliente.cpf
        cliente.telefone = telefone or cliente.telefone
        return self.cliente_dao.update(cliente)

    def deletar(self, id):
        """
        Deleta um cliente pelo seu ID.

        :param id: ID do cliente a ser deletado.
        :return: Resultado da operação de exclusão.
        """
        return self.cliente_dao.delete(id)

    def find_by_id(self, id):
        """
        Busca um cliente pelo seu ID.

        :param id: ID do cliente.
        :return: Cliente encontrado ou None.
        """
        return self.cliente_dao.find_by_id(id)

    def listar(self):
        """
        Lista todos os clientes cadastrados.

        :return: Lista de clientes.
        """
        return self.cliente_dao.find_all()
