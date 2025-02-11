from view.MenuEntity import MenuEntity

from util.StringUtil import is_blank
from util.NumberUtil import get_int, get_float

from model.Produto import Produto

from controller.ProdutoController import ProdutoController
from controller.CategoriaController import CategoriaController

from termcolor import colored

class MenuProduto(MenuEntity):
    def __init__(self):
        super().__init__()
        self.produto_controller = ProdutoController()
        self.categoria_controller = CategoriaController()
        
    def showTitle(self, title=""):
        return super().showTitle("Produtos")
        
    def atualizar(self):
        super().showTitle("Atualizar Produto")
        
        produto = Produto()
        
        while True:
            id = get_int(self.getSuccessMessage("ID do produto: "), min=0)
            
            produto = self.produto_controller.find_by_id(id)
            
            if produto is None:
                print(self.getErrorMessage("Erro: Produto não encontrado, tente novamente"))
                continue
            else:
                break
            
        nome = input(self.getSuccessMessage("Novo Nome (deixe em branco para manter o atual): "))
        preco = get_float(self.getSuccessMessage("Novo Preço: "), min=0)
        
        self.mostrarCategorias()
        
        categoria = None
        
        while True:
            id = get_int(self.getSuccessMessage("ID da categoria do produto: "), min=0)
            
            categoria = self.categoria_controller.find_by_id(id)
            
            if categoria is None:
                print(self.getErrorMessage("Erro: Categoria não encontrada, tente novamente"))
                continue
            else:
                break
        
        
        quantidade = get_int(self.getSuccessMessage("Nova Quantidade: "), min=0)
        unidade_medida = input(self.getSuccessMessage("Nova Unidade de Medida (deixe em branco para manter a atual): "))

        produto.nome = nome or produto.nome
        produto.preco = preco or produto.preco
        produto.quantidade = quantidade or produto.quantidade
        produto.unidadeMedida = unidade_medida or produto.unidadeMedida
        produto.categoria = categoria
        
        is_produto_atualizado = self.produto_controller.update(produto)
        
        if is_produto_atualizado:
            print(colored("\nProduto atualizado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao atualizar o produto.", 'red', attrs=['bold']))
    
    def mostrarCategorias(self):
        categorias = self.categoria_controller.find_all()
        
        print(self.getBlueMessage("===Categorias"))
        
        for categoria in categorias:
            print(colored(f"[{categoria.id}] {categoria.nome}", 'light_blue', attrs=['bold']))
            

    def cadastrar(self):
        super().showTitle("Cadastrar Produto")
        
        super().showTitle("Atualizar Produto")
        
        produto = Produto()
            
        nome = input(self.getSuccessMessage("Nome produto: "))
        preco = get_float(self.getSuccessMessage("Preço: "), min=0)
        
        self.mostrarCategorias()
        
        categoria = None
        
        while True:
            id = get_int(self.getSuccessMessage("ID da categoria do produto: "), min=0)
            
            categoria = self.categoria_controller.find_by_id(id)
            
            if categoria is None:
                print(self.getErrorMessage("Erro: Categoria não encontrada, tente novamente"))
                continue
            else:
                break
        
        
        quantidade = get_int(self.getSuccessMessage("Quantidade: "), min=0)
        unidade_medida = input(self.getSuccessMessage("Unidade de Medida: "))

        produto.nome = nome
        produto.preco = preco
        produto.quantidade = quantidade
        produto.unidadeMedida = unidade_medida
        produto.categoria = categoria
        
        is_produto_cadastrado = self.produto_controller.save(produto)
        
        if is_produto_cadastrado:
            print(colored("\nProduto cadastrado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao cadastrar o produto.", 'red', attrs=['bold']))
    
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