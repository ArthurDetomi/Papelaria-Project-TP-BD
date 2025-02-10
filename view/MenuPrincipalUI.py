from view.MenuAbstrato import MenuAbstrato
from view.MenuVendaUI import MenuVendaUI
from view.MenuFormaPagamento import MenuFormaPagamento

from service.UserSession import UserSession

from termcolor import colored

class MenuPrincipal(MenuAbstrato):
    def __init__(self):
        super().__init__()
        self.menu_venda_ui = MenuVendaUI()
        self.menu_forma_pagamento_ui = MenuFormaPagamento()

    def showTitle(self):
        user_login = UserSession.getLoggedUser().login

        print(colored("=====================================", 'cyan'))
        print(colored(f"    Bem-vindo(a) ao Sistema da Papelaria Papel & Arte, {user_login}!", 'yellow', attrs=['bold']))
        print(colored("=====================================", 'cyan'))
        print("\nO que você deseja fazer hoje?\n")

    def runOption(self, option : int):
        if option == 0:
            return 0
        elif option == 1:
            print("Ainda não implementado!")
        elif option == 2:
            self.menu_venda_ui.mostrarMenu()
        elif option == 3:
            print("Ainda não implementado!")
        elif option == 4:
            print("Ainda não implementado!")
        elif option == 5:
            self.menu_forma_pagamento_ui.mostrarMenu()
        elif option == 6:
            print("Ainda não implementado!")



    def showOptions(self):
        print(colored("[0] Sair do Programa", 'red', attrs=['bold']))
        print(colored("[1] Gerenciar Produtos", 'green'))
        print(colored("[2] Gerenciar Vendas", 'green'))
        print(colored("[3] Gerenciar Usuários", 'green'))
        print(colored("[4] Gerenciar Categorias", 'green'))
        print(colored("[5] Gerenciar Formas de Pagamento", 'green'))
        print(colored("[6] Gerenciar Clientes", 'green'))

