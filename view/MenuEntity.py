from view.MenuAbstrato import MenuAbstrato
from termcolor import colored

class MenuEntity(MenuAbstrato):

    def listar(self):
        raise NotImplementedError()

    def cadastrar(self):
        raise NotImplementedError()

    def remover(self):
        raise NotImplementedError()


    def runOption(self, option: int):
        if option == 0:
            return 0
        elif option == 1:
            self.cadastrar()
        elif option == 2:
            self.listar()
        elif option == 3:
            self.remover()

    def showOptions():
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))

