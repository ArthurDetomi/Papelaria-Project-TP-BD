from view.MenuEntity import MenuEntity

from util.StringUtil import is_blank
from util.NumberUtil import get_int

from datetime import datetime

from termcolor import colored

class MenuCliente(MenuEntity):
    
    def cadastrar(self):
        return super().cadastrar()
    
    def listar(self):
        return super().listar()
    
    def remover(self):
        return super().remover()
    
    def atualizar():
        pass
     
    def showOptions(self):
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))
        print(colored("[4] Atualizar", 'green'))


    def runOption(self, option: int):
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
            print(colored("Opção Inválida!", 'red', attrs=['bold']))