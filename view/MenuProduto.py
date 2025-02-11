from view.MenuEntity import MenuEntity

from util.StringUtil import is_blank
from util.NumberUtil import get_int

from controller.ProdutoController import ProdutoController

from termcolor import colored

class MenuProduto(MenuEntity):
    def __init__(self):
        super().__init__()
        self.produto_controller = ProdutoController()
        
    def atualizar(self):
        super().showTitle("Atualizar Produto")
        
        id = input(self.getSuccessMessage("ID do produto: "))
        nome = input(self.getSuccessMessage("Novo Nome (deixe em branco para manter o atual): "))
        preco = input(self.getSuccessMessage("Novo Preço (deixe em branco para manter o atual): "))
        categoria = input(self.getSuccessMessage("Nova Categoria (deixe em branco para manter a atual): "))
        quantidade = input(self.getSuccessMessage("Nova Quantidade (deixe em branco para manter a atual): "))
        unidade_medida = input(self.getSuccessMessage("Nova Unidade de Medida (deixe em branco para manter a atual): "))
        
        print("Falta terminar implementação")
        
        

    def cadastrar(self):
        super().showTitle("Cadastrar Produto")
        
        nome = input(self.getSuccessMessage("Nome: "))
        preco = input(self.getSuccessMessage("Preço: "))
        categoria = input(self.getSuccessMessage("Categoria: "))
        quantidade = input(self.getSuccessMessage("Quantidade em estoque: "))
        unidade_medida = input(self.getSuccessMessage("Unidade de Medida: "))
        
        print("Falta terminar implementação")
    
    def remover(self):
        super().showTitle("Deletar Produto")
        
        id = input(self.getSuccessMessage("ID do produto: "))

        produto = self.produto_controller.find_by_id(id)
        
        if (produto == None):
            print(self.getErrorMessage('\nProduto não encontrado.'))
            return
        
        is_produto_deletado = self.produto_controller.deletar(id)
        
        if is_produto_deletado:
            print(colored("\nProduto deletado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao deletar o produto.", 'red', attrs=['bold']))
    
    def listar(self):
        super().showTitle("Lista de produtos")
    
        produtos = self.produto_controller.listar()
        if produtos:
            for produto in produtos:
                print(produto)
        else:
            print(self.getErrorMessage("Nenhum produto cadastrado"))
    
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