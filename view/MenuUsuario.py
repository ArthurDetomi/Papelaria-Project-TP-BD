from view.MenuEntity import MenuEntity

from util.StringUtil import is_blank
from util.NumberUtil import get_int

from controller.UsuarioController import UsuarioController

from datetime import datetime

from termcolor import colored

class MenuUsuario(MenuEntity):
    
    def __init__(self):
        super().__init__()
        self.usuario_controller = UsuarioController()
    
    def showTitle(self):
        super().showTitle("Usuarios")
    
    def cadastrar(self):
        super().showTitle("Cadastrar Usuarios")
        
        print(colored("=== Preencha as credenciais ===\n", 'blue'))
        
        login = input(colored("Login: ", 'green'))
        senha = input(colored("Senha: ", 'green'))
        cpf = input(colored("CPF: ", 'green'))

        is_usuario_cadastrado = self.usuario_controller.cadastrar_usuario(login=login, senha=senha, cpf=cpf)
        
        if is_usuario_cadastrado:
            print(colored("\nUsuário cadastrado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao cadastrar o usuário.", 'red', attrs=['bold']))
            
    def listar(self):
        super().showTitle("Lista de Usuários")
    
        usuarios = self.usuario_controller.listar_usuarios()
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print(self.getErrorMessage("Nenhum usuario cadastrado"))
    
    def remover(self):
        super().showTitle("Deletar Usuário")
        
        id = input(self.getSuccessMessage("ID do usuário: "))

        usuario = self.usuario_controller.find_by_id(id)
        
        if (usuario == None):
            print(self.getErrorMessage('\nUsuário não encontrado.'))
            return
        
        is_usuario_deletado = self.usuario_controller.deletar_usuario(id)
        
        if is_usuario_deletado:
            print(colored("\nUsuário deletado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao deletar o usuário.", 'red', attrs=['bold']))
        
    def atualizar(self):
        super().showTitle("Atualizar Usuário")
        id = int(input(self.getSuccessMessage("ID do usuário: ")))
        login = input(self.getSuccessMessage("Novo Login (deixe em branco para manter o atual): "))
        senha = input(self.getSuccessMessage("Nova Senha (deixe em branco para manter a atual): "))
        cpf = input(self.getSuccessMessage("Novo CPF (deixe em branco para manter o atual): "))

        usuario = self.usuario_controller.find_by_id(id)
        
        if (usuario == None):
            print(self.getErrorMessage('\nUsuário não encontrado.'))
            return
        
        is_usuario_atualizado = self.usuario_controller.atualizar_usuario(id, login, senha, cpf)
        
        if is_usuario_atualizado:
            print(colored("\nUsuário atualizado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao atualizar o usuário.", 'red', attrs=['bold']))
     
    
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