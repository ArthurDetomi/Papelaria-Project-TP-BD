from controller.UsuarioController import UsuarioController
import pwinput
from termcolor import colored

class LoginUi:
    def __init__(self):
        self.usuario_controller = UsuarioController()

    def showMenu(self):
        print("\033[1;33mBem-vindo à Papelaria Papel & Arte!\033[0m")
        print("\033[1;34mFaça seu login abaixo:\033[0m")

        while True:
            login = input("\033[1;32mLogin: \033[0m")
            senha = pwinput.pwinput("\033[1;32mSenha: \033[0m")

            print("Validando credencias...")

            if self.usuario_controller.realizarLogin(login, senha):
                print(colored("Login realizado com sucesso!", 'green', attrs=['bold']))
                break
            else:
                print(colored("Credenciais inválidas, tente novamente", 'red', attrs=['bold']))
                continue

