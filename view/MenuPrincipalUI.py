"""Módulo MenuPrincipalUI.

Fornece a interface do menu principal do sistema, permitindo acesso a
diversos módulos, como produtos, vendas, usuários, categorias,
formas de pagamento e clientes.
"""

from view.MenuAbstrato import MenuAbstrato
from view.MenuVendaUI import MenuVendaUI
from view.MenuFormaPagamento import MenuFormaPagamento
from view.MenuCliente import MenuCliente
from view.MenuUsuario import MenuUsuario
from view.MenuCategoria import MenuCategoria
from view.MenuProduto import MenuProduto
from service.UserSession import UserSession
from termcolor import colored


class MenuPrincipal(MenuAbstrato):
    """Menu principal do sistema Papelaria Papel & Arte."""

    def __init__(self):
        super().__init__()
        self.menu_venda_ui = MenuVendaUI()
        self.menu_forma_pagamento_ui = MenuFormaPagamento()
        self.menu_categoria_ui = MenuCategoria()
        self.menu_usuario_ui = MenuUsuario()
        self.menu_cliente_ui = MenuCliente()
        self.menu_produto_ui = MenuProduto()

    def show_title(self, title=""):
        """
        Exibe o título do menu principal, com boas-vindas ao usuário logado.
        """
        user_login = UserSession.get_logged_user().login

        print(colored("=====================================", 'cyan'))
        print(colored(f"    Bem-vindo(a) ao Sistema da Papelaria Papel & Arte, {user_login}!", 'yellow', attrs=['bold']))
        print(colored("=====================================", 'cyan'))
        print("\nO que você deseja fazer hoje?\n")

    def run_option(self, option: int):
        """
        Executa a opção selecionada no menu principal.

        :param option: Opção selecionada.
        :return: 0 se for sair; caso contrário, encaminha para o menu correspondente.
        """
        if option == 0:
            return 0
        elif option == 1:
            self.menu_produto_ui.show_menu()
        elif option == 2:
            self.menu_venda_ui.show_menu()
        elif option == 3:
            self.menu_usuario_ui.show_menu()
        elif option == 4:
            self.menu_categoria_ui.show_menu()
        elif option == 5:
            self.menu_forma_pagamento_ui.show_menu()
        elif option == 6:
            self.menu_cliente_ui.show_menu()
        else:
            print(self.get_error_message("Opção selecionada não existe"))

    def show_options(self):
        """Exibe as opções do menu principal."""
        print(colored("[0] Sair do Programa", 'red', attrs=['bold']))
        print(colored("[1] Gerenciar Produtos", 'green'))
        print(colored("[2] Gerenciar Vendas", 'green'))
        print(colored("[3] Gerenciar Usuários", 'green'))
        print(colored("[4] Gerenciar Categorias", 'green'))
        print(colored("[5] Gerenciar Formas de Pagamento", 'green'))
        print(colored("[6] Gerenciar Clientes", 'green'))
