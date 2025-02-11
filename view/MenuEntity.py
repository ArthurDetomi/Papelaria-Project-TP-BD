"""Módulo MenuEntity.

Define a classe abstrata MenuEntity, que estende MenuAbstrato e fornece
a estrutura base para menus de entidades, como cadastro, listagem e remoção.
"""

from view.MenuAbstrato import MenuAbstrato
from termcolor import colored


class MenuEntity(MenuAbstrato):
    """
    Classe base para menus de entidades.
    
    Métodos abstratos:
      - listar()
      - cadastrar()
      - remover()
    """

    def listar(self):
        raise NotImplementedError("O método listar() deve ser implementado.")

    def cadastrar(self):
        raise NotImplementedError("O método cadastrar() deve ser implementado.")

    def remover(self):
        raise NotImplementedError("O método remover() deve ser implementado.")

    def run_option(self, option: int):
        """
        Executa a opção selecionada no menu da entidade.

        :param option: Opção selecionada.
        :return: 0 se for a opção de sair; caso contrário, executa a ação.
        """
        if option == 0:
            return 0
        elif option == 1:
            self.cadastrar()
        elif option == 2:
            self.listar()
        elif option == 3:
            self.remover()
        else:
            print(colored("Opção inválida!", 'red', attrs=['bold']))

    def show_options(self):
        """Exibe as opções disponíveis no menu da entidade."""
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))
