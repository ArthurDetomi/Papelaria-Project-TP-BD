from view.MenuEntity import MenuEntity

from util.StringUtil import is_blank
from util.NumberUtil import get_int

from controller.ClienteController import ClienteController

from datetime import datetime

from termcolor import colored

class MenuCliente(MenuEntity):
    
    def __init__(self):
        super().__init__()
        self.cliente_controller = ClienteController()
    
    def cadastrar(self):
        super().showTitle("Cadastrar Cliente")
        
        nome = input(self.getSuccessMessage("Nome: "))
        cpf = input(self.getSuccessMessage("CPF: "))
        telefone = input(self.getSuccessMessage("Telefone: "))

        is_cliente_cadastrado = self.cliente_controller.cadastrar_cliente(nome=nome, cpf=cpf, telefone=telefone)
        
        if is_cliente_cadastrado:
            print(colored("\nCliente cadastrado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao cadastrar o cliente.", 'red', attrs=['bold']))
        
        
    
    def listar(self):
        super().showTitle("Lista de Clientes")
    
        clientes = self.cliente_controller.listar()
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print(self.getErrorMessage("Nenhum cliente cadastrado"))
    
    def remover(self):
        super().showTitle("Deletar Cliente")
        
        id = input(self.getSuccessMessage("ID do cliente: "))

        cliente = self.cliente_controller.find_by_id(id)
        
        if (cliente == None):
            print(self.getErrorMessage('\nCliente não encontrado.'))
            return
        
        is_cliente_deletado = self.cliente_controller.deletar(id)
        
        if is_cliente_deletado:
            print(colored("\nCliente deletado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao deletar o cliente.", 'red', attrs=['bold']))
    
    def atualizar(self):
        super().showTitle("Atualizar Cliente")
        
        id = input(self.getSuccessMessage("ID do cliente: "))
        nome = input(self.getSuccessMessage("Novo Nome (deixe em branco para manter o atual): "))
        cpf = input(self.getSuccessMessage("Novo CPF (deixe em branco para manter o atual): "))
        telefone = input(self.getSuccessMessage("Novo Telefone (deixe em branco para manter o atual): "))
        
        is_cliente_atualizado = self.cliente_controller.atualizar_cliente(id=id, nome=nome, cpf=cpf, telefone=telefone)
        
        if is_cliente_atualizado:
            print(colored("\nCliente atualizado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao atualizar cliente.", 'red', attrs=['bold']))
     
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