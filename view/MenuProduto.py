"""Módulo MenuProduto.

Fornece a interface de menu para o gerenciamento de produtos, permitindo o
cadastro, listagem, remoção e atualização dos produtos.
"""

from view.MenuEntity import MenuEntity
from util.NumberUtil import get_int, get_float
from controller.ProdutoController import ProdutoController
from controller.CategoriaController import CategoriaController
from termcolor import colored


class MenuProduto(MenuEntity):
    """Menu interativo para operações relacionadas a produtos."""

    def __init__(self):
        super().__init__()
        self.produto_controller = ProdutoController()
        self.categoria_controller = CategoriaController()

    def show_title(self, title=""):
        """Exibe o título do menu de produtos."""
        return super().show_title("Produtos")

    def mostrar_categorias(self):
        """Exibe categorias disponíveis"""
        categorias = self.categoria_controller.find_all()
        
        print(self.get_blue_message("===Categorias"))
        
        for categoria in categorias:
            print(colored(f"[{categoria.id}] {categoria.nome}", 'light_blue', attrs=['bold']))

    def atualizar(self):
        """
        Atualiza os dados de um produto existente.
        
        Solicita os novos valores e envia os dados atualizados para o controlador.
        """
        super().show_title("Atualizar Produto")

        id_produto = get_int(self.get_success_message("ID do produto: "))

        produto_obj = self.produto_controller.find_by_id(id_produto)
        while produto_obj is None:
            self.get_error_message("Digite o ID de um produto válido!")
            id_produto = get_int(self.get_success_message("ID do produto: "))
            produto_obj = self.produto_controller.find_by_id(id_produto)

        novo_nome = input(self.get_success_message("Novo Nome (deixe em branco para manter o atual): "))
        if novo_nome:
            produto_obj.nome = novo_nome
        
        novo_preco = input(self.get_success_message("Novo Preço (deixe em branco para manter o atual): "))
        if novo_preco:
            try:
                produto_obj.preco = float(novo_preco)
            except ValueError:
                self.get_error_message("Valor digitado não válido. Preço não atualizado!\n")
        
        self.mostrar_categorias()
        nova_categoria = input(self.get_success_message("Nova Categoria (deixe em branco para manter a atual): "))
        if nova_categoria:
            try:
                categoria_int = int(nova_categoria)
                categoria_obj = self.categoria_controller.find_by_id(categoria_int)
                while categoria_obj is None:
                    self.get_error_message("Categoria inválida, digite o ID de uma categoria existente!")
                    nova_categoria = input(self.get_success_message("Nova Categoria (deixe em branco para manter a atual): "))
                    categoria_int = int(nova_categoria)
                    categoria_obj = self.categoria_controller.find_by_id(categoria_int)
                produto_obj.categoria = categoria_obj
            except ValueError:
                self.get_error_message("Valor digitado não é um número. Categoria não atualizada")

        nova_quantidade = input(self.get_success_message("Nova Quantidade (deixe em branco para manter a atual): "))
        if nova_quantidade:
            try:
                nova_quantidade_int = int(nova_quantidade)
                produto_obj.quantidade = nova_quantidade_int
            except ValueError:
                self.get_error_message("Valor digitado não válido. Quantidade não atualizado!\n")
        
        nova_unidade = input(self.get_success_message("Nova Unidade de Medida (deixe em branco para manter a atual): "))
        if nova_unidade:
            produto_obj.unidade_medida = nova_unidade
        if self.produto_controller.atualizar_produto(
                                id=produto_obj.id,
                                nome=produto_obj.nome,
                                preco=produto_obj.preco,
                                categoria=produto_obj.categoria.id,
                                quantidade=produto_obj.quantidade,
                                unidade_medida=produto_obj.unidade_medida
                            ):
            print(colored("\nProduto atualizado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao atualizar o produto.", 'red', attrs=['bold']))

    def cadastrar(self):
        """
        Realiza o cadastro de um novo produto, solicitando os dados necessários.
        """
        super().show_title("Cadastrar Produto")

        nome = input(self.get_success_message("Nome: "))
        preco = get_float(self.get_success_message("Preço: "))
        self.mostrar_categorias()
        categoria = get_int(self.get_success_message("Categoria: "))
        categoria_obj = self.categoria_controller.find_by_id(categoria)
        while categoria_obj is None:
            print(self.get_error_message("Erro: Categoria não encontrada, digite uma categoria válida!"))
            categoria = get_int(self.get_success_message("Categoria: "))
            categoria_obj = self.categoria_controller.find_by_id(categoria)
        quantidade = get_int(self.get_success_message("Quantidade em estoque: "))
        unidade_medida = input(self.get_success_message("Unidade de Medida: "))

        self.produto_controller.cadastrar_produto(
            nome=nome,
            preco=preco,
            categoria=categoria,
            quantidade=quantidade,
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
