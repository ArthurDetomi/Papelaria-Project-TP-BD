"""Módulo MenuProduto.

Fornece a interface de menu para o gerenciamento de produtos, permitindo o
cadastro, listagem, remoção e atualização dos produtos.
"""

from view.MenuEntity import MenuEntity
from util.NumberUtil import get_int, get_float
from controller.ProdutoController import ProdutoController
from termcolor import colored


class MenuProduto(MenuEntity):
    """Menu interativo para operações relacionadas a produtos."""

    def __init__(self):
        super().__init__()
        self.produto_controller = ProdutoController()

    def show_title(self, title=""):
        """Exibe o título do menu de produtos."""
        return super().show_title("Produtos")

    def atualizar(self):
        """
        Atualiza os dados de um produto existente.
        
        Solicita os novos valores e envia os dados atualizados para o controlador.
        """
        super().show_title("Atualizar Produto")

        id_produto = input(self.get_success_message("ID do produto: "))
        novo_nome = input(self.get_success_message("Novo Nome (deixe em branco para manter o atual): "))
        novo_preco = input(self.get_success_message("Novo Preço (deixe em branco para manter o atual): "))
        nova_categoria = input(self.get_success_message("Nova Categoria (deixe em branco para manter a atual): "))
        nova_quantidade = input(self.get_success_message("Nova Quantidade (deixe em branco para manter a atual): "))
        nova_unidade = input(self.get_success_message("Nova Unidade de Medida (deixe em branco para manter a atual): "))

        self.produto_controller.atualizar_produto(
            id=get_int(id_produto),
            nome=novo_nome,
            preco=get_float(novo_preco),
            categoria=get_int(nova_categoria),
            quantidade=get_int(nova_quantidade),
            unidade_medida=nova_unidade
        )

    def cadastrar(self):
        """
        Realiza o cadastro de um novo produto, solicitando os dados necessários.
        """
        super().show_title("Cadastrar Produto")

        nome = input(self.get_success_message("Nome: "))
        preco = input(self.get_success_message("Preço: "))
        categoria = input(self.get_success_message("Categoria: "))
        quantidade = input(self.get_success_message("Quantidade em estoque: "))
        unidade_medida = input(self.get_success_message("Unidade de Medida: "))

        self.produto_controller.cadastrar_produto(
            nome=nome,
            preco=float(preco),
            categoria=int(categoria),
            quantidade=int(quantidade),
            unidade_medida=unidade_medida,
        )

    def remover(self):
        """
        Remove um produto a partir do seu ID.
        """
        super().show_title("Deletar Produto")

        id_produto = input(self.get_success_message("ID do produto: "))
        produto = self.produto_controller.find_by_id(id_produto)

        if produto is None:
            print(self.get_error_message("\nProduto não encontrado."))
            return

        is_produto_deletado = self.produto_controller.deletar(id_produto)
        if is_produto_deletado:
            print(colored("\nProduto deletado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao deletar o produto.", 'red', attrs=['bold']))

    def listar(self):
        """
        Lista todos os produtos cadastrados e os exibe.
        """
        super().show_title("Lista de Produtos")

        produtos = self.produto_controller.listar()
        if produtos:
            for produto in produtos:
                print(produto)
        else:
            print(self.get_error_message("Nenhum produto cadastrado"))

    def show_options(self):
        """Exibe as opções disponíveis no menu de produtos."""
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))
        print(colored("[4] Atualizar", 'green'))

    def run_option(self, option: int):
        """
        Executa a opção selecionada no menu de produtos.

        :param option: Opção selecionada.
        :return: 0 se for sair; caso contrário, executa a ação correspondente.
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
