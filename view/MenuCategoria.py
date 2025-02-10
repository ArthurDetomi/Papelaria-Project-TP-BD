from view.MenuEntity import MenuEntity

from controller.CategoriaController import CategoriaController

from util.StringUtil import is_blank
from util.NumberUtil import get_int

from datetime import datetime

from termcolor import colored

class MenuCategoria(MenuEntity):
    def __init__(self):
        super().__init__()
        self.categoria_controller = CategoriaController()

    def showTitle(self):
        super().showTitle("categoria")

    def cadastrar(self):
        super().showTitle("Cadastro de categoria")

        while True:
            nome = input(colored("Nome da categoria: ", 'green'))

            if is_blank(nome):
                print("Erro: Nome de categoria não pode ser vazio!")
                return

            try:
                is_categoria_cadastrada = self.categoria_controller.cadastrar(nome)
            except Exception as e:
                print(colored(f"\nErro: {e}\n", 'red'))
                print(colored("Ocorreu um erro inesperado ao cadastrar a categoria.", 'red'))

            if is_categoria_cadastrada:
                print(colored("\nCategoria cadastrada com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao cadastrar a categoria.", 'red', attrs=['bold']))

            print(colored("\nDeseja cadastrar mais categorias?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)

            if opcao == 0:
                break

    def remover(self):
        super().showTitle("Deletar categoria")

        while True:
            id_categoria = get_int(msg="Informe o id da categoria:", min=1)

            is_success = self.categoria_controller.deletar(id_categoria)

            if is_success:
                print(colored("\nCategoria removida com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao deletar a categoria.", 'red', attrs=['bold']))

            print(colored("\nDeseja deletar mais categoriass?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)

            if opcao == 0:
                break

    def listar(self):
        super().showTitle("Listar categorias")

        categorias = self.categoria_controller.find_all()

        if categorias:
            for categoria in categorias:
                print(categoria)
        else:
            print(colored("Nenhuma categoria cadastrada.", 'red', attrs=['bold']))

    def atualizar(self):
        super().showTitle("Atualizar categoria")

        id = get_int(msg="Informe o id da categoria:", min=1)

        categoria = self.categoria_controller.find_by_id(id)

        if categoria is not None:
            print(colored(f"\ncategoria: {categoria.nome}", 'cyan', attrs=['bold']))

            nome = input(colored("\nNova categoria: ", 'green'))

            if nome == "":
                categoria.nome = categoria.nome
            else:
                categoria.nome = nome
                editado = datetime.now()
                categoria.editado = editado

            is_categoria_atualizada = self.categoria_controller.atualizar(categoria)

            if is_categoria_atualizada:
                print(colored("\ncategoria atualizada com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao atualizar a categoria.", 'red', attrs=['bold']))
        else:
            print(colored("\ncategoria nao encontrada.", 'red', attrs=['bold']))

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





