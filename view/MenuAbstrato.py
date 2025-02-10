from termcolor import colored
from util.NumberUtil import get_int

class MenuAbstrato:
    def mostrarMenu(self):
        while True:
            self.showTitle()

            self.showOptions()

            option = get_int(msg="Informe sua opção: ", min=0)

            option_selected = self.runOption(option)

            if option_selected == 0:
                print(colored("Fim do programa", 'light_red', attrs=['bold']))
                print(colored("Obrigado por usar o sistema! Até a próxima!", 'green', attrs=['bold']))
                break

    def showTitle(self, title=""):
        print(colored("="*40, 'cyan'))
        print(colored(f"    {title}", 'yellow', attrs=['bold']))
        print(colored("="*40, 'cyan'))

    def runOption(self, option : int):
        raise NotImplementedError()

    def showOptions(self):
        raise NotImplementedError()

