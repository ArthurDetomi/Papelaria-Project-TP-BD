"""Módulo LoginUI.

Contém a classe LoginUI, que é responsável por apresentar a interface de
login ao usuário, coletar as credenciais e validá-las através do
controlador de usuário.
"""

from controller.UsuarioController import UsuarioController
import pwinput
from termcolor import colored


class LoginUI:
    """Interface de login do sistema Papelaria Papel & Arte."""

    def __init__(self):
        """Inicializa o controlador de usuário."""
        self.usuario_controller = UsuarioController()

    def show_menu(self):
        """
        Exibe o menu de login, solicita as credenciais e valida o acesso.
        
        O método continua solicitando o login até que as credenciais sejam válidas.
        """
        print("\033[1;33mBem-vindo à Papelaria Papel & Arte!\033[0m")
        print("\033[1;34mFaça seu login abaixo:\033[0m")

        while True:
            login = input("\033[1;32mLogin: \033[0m")
            senha = pwinput.pwinput("\033[1;32mSenha: \033[0m")

            print("Validando credenciais...")

            if self.usuario_controller.realizar_login(login, senha):
                print(colored("Login realizado com sucesso!", 'green', attrs=['bold']))
                break
            else:
                print(colored("Credenciais inválidas, tente novamente", 'red', attrs=['bold']))
