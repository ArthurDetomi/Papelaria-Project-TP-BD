"""Módulo MenuCategoria.

Fornece a interface de menu para o gerenciamento de categorias, permitindo
o cadastro, listagem, remoção e atualização de categorias.
"""

from view.MenuEntity import MenuEntity
from controller.CategoriaController import CategoriaController
from util.StringUtil import is_blank
from util.NumberUtil import get_int
from datetime import datetime
from termcolor import colored


class MenuCategoria(MenuEntity):
    """Menu interativo para operações relacionadas à categoria."""

    def __init__(self):
        super().__init__()
        self.categoria_controller = CategoriaController()

    def show_title(self, title="Categoria"):
        """Exibe o título do menu de categoria."""
        super().show_title(title)

    def cadastrar(self):
        """
        Realiza o cadastro de uma nova categoria.
        
        Solicita o nome da categoria e exibe mensagens de sucesso ou erro.
        """
        super().show_title("Cadastro de Categoria")

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
                return

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
        """
        Remove uma categoria a partir do seu ID.
        
        Exibe mensagem de sucesso ou falha e permite a remoção de múltiplas categorias.
        """
        super().show_title("Deletar Categoria")

        while True:
            id_categoria = get_int(msg="Informe o id da categoria: ", min=1)

            is_success = self.categoria_controller.deletar(id_categoria)

            if is_success:
                print(colored("\nCategoria removida com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao deletar a categoria.", 'red', attrs=['bold']))

            print(colored("\nDeseja deletar mais categorias?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)
            if opcao == 0:
                break

    def listar(self):
        """
        Lista todas as categorias cadastradas e as exibe na tela.
        """
        super().show_title("Listar Categorias")

        categorias = self.categoria_controller.find_all()

        if categorias:
            for categoria in categorias:
                print(categoria)
        else:
            print(colored("Nenhuma categoria cadastrada.", 'red', attrs=['bold']))

    def atualizar(self):
        """
        Atualiza uma categoria existente a partir do seu ID.
        
        Solicita o novo nome e atualiza a data de edição.
        """
        super().show_title("Atualizar Categoria")

        id_categoria = get_int(msg="Informe o id da categoria: ", min=1)

        categoria = self.categoria_controller.find_by_id(id_categoria)

        if categoria is not None:
            print(colored(f"\nCategoria: {categoria.nome}", 'cyan', attrs=['bold']))

            novo_nome = input(colored("\nNova categoria: ", 'green'))
            if novo_nome.strip():
                categoria.nome = novo_nome
                categoria.editado = datetime.now()

            is_categoria_atualizada = self.categoria_controller.atualizar(categoria)

            if is_categoria_atualizada:
                print(colored("\nCategoria atualizada com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao atualizar a categoria.", 'red', attrs=['bold']))
        else:
            print(colored("\nCategoria não encontrada.", 'red', attrs=['bold']))

    def show_options(self):
        """Exibe as opções disponíveis no menu de categoria."""
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))
        print(colored("[4] Atualizar", 'green'))

    def run_option(self, option: int):
        """
        Executa a opção selecionada no menu de categoria.

        :param option: Opção selecionada.
        :return: 0 se a opção for sair; caso contrário, executa a ação correspondente.
        """
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
            print(colored("Opção inválida!", 'red', attrs=['bold']))
