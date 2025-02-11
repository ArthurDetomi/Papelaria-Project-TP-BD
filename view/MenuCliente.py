"""Módulo MenuCliente.

Fornece a interface de menu para o gerenciamento de clientes, permitindo o
cadastro, listagem, remoção e atualização dos dados dos clientes.
"""

from view.MenuEntity import MenuEntity
from util.StringUtil import is_blank
from util.NumberUtil import get_int
from controller.ClienteController import ClienteController
from datetime import datetime
from termcolor import colored


class MenuCliente(MenuEntity):
    """Menu interativo para operações relacionadas a clientes."""

    def __init__(self):
        super().__init__()
        self.cliente_controller = ClienteController()

    def cadastrar(self):
        """
        Realiza o cadastro de um novo cliente, solicitando nome, CPF e telefone.
        """
        super().show_title("Cadastrar Cliente")

        nome = input(self.get_success_message("Nome: "))
        cpf = input(self.get_success_message("CPF: "))
        telefone = input(self.get_success_message("Telefone: "))

        is_cliente_cadastrado = self.cliente_controller.cadastrar_cliente(
            nome=nome, cpf=cpf, telefone=telefone
        )

        if is_cliente_cadastrado:
            print(colored("\nCliente cadastrado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao cadastrar o cliente.", 'red', attrs=['bold']))

    def listar(self):
        """
        Exibe a lista de clientes cadastrados.
        """
        super().show_title("Lista de Clientes")

        clientes = self.cliente_controller.listar()
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print(self.get_error_message("Nenhum cliente cadastrado"))

    def remover(self):
        """
        Remove um cliente com base no ID informado.
        """
        super().show_title("Deletar Cliente")

        id_cliente = input(self.get_success_message("ID do cliente: "))

        cliente = self.cliente_controller.find_by_id(id_cliente)
        if cliente is None:
            print(self.get_error_message("\nCliente não encontrado."))
            return

        is_cliente_deletado = self.cliente_controller.deletar(id_cliente)
        if is_cliente_deletado:
            print(colored("\nCliente deletado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao deletar o cliente.", 'red', attrs=['bold']))

    def atualizar(self):
        """
        Atualiza os dados de um cliente existente, permitindo modificar nome, CPF e telefone.
        """
        super().show_title("Atualizar Cliente")

        id_cliente = input(self.get_success_message("ID do cliente: "))
        novo_nome = input(self.get_success_message("Novo Nome (deixe em branco para manter o atual): "))
        novo_cpf = input(self.get_success_message("Novo CPF (deixe em branco para manter o atual): "))
        novo_telefone = input(self.get_success_message("Novo Telefone (deixe em branco para manter o atual): "))

        is_cliente_atualizado = self.cliente_controller.atualizar_cliente(
            id=id_cliente, nome=novo_nome, cpf=novo_cpf, telefone=novo_telefone
        )

        if is_cliente_atualizado:
            print(colored("\nCliente atualizado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao atualizar o cliente.", 'red', attrs=['bold']))

    def show_options(self):
        """Exibe as opções disponíveis no menu de cliente."""
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))
        print(colored("[4] Atualizar", 'green'))

    def run_option(self, option: int):
        """
        Executa a opção selecionada no menu de cliente.

        :param option: Opção selecionada.
        :return: 0 se a opção for sair; caso contrário, executa a ação correspondente.
        """
        if option == 0:
            return 0
        elif option == 1:
            self.cadastrar()
        elif option == 2:
            self.listar()
        elif option == 3:
            self.remover()
        elif option == 4:
            self.atualizar()
        else:
            print(colored("Opção inválida!", 'red', attrs=['bold']))
