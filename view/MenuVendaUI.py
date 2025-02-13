"""Módulo MenuVendaUI.

Fornece a interface de menu para o gerenciamento de vendas, permitindo
o cadastro, listagem e remoção de vendas, além de gerenciar a inserção de itens,
cliente e forma de pagamento.
"""

from view.MenuEntity import MenuEntity
from termcolor import colored
from model.Item import Item
from model.Venda import Venda
from service.UserSession import UserSession
from controller.VendaController import VendaController
from controller.ProdutoController import ProdutoController
from controller.ClienteController import ClienteController
from controller.ItemController import ItemController
from controller.FormaPagamentoController import FormaPagamentoController
from util.NumberUtil import get_int, get_float


class MenuVendaUI(MenuEntity):
    """Menu interativo para operações relacionadas a vendas."""

    def __init__(self):
        super().__init__()
        self.venda_controller = VendaController()
        self.produto_controller = ProdutoController()
        self.item_controller = ItemController()
        self.forma_pagamento_controller = FormaPagamentoController()
        self.cliente_controller = ClienteController()

    def show_title(self, title="Venda"):
        """Exibe o título do menu de vendas."""
        super().show_title(title)

    def cadastrar(self):
        """
        Realiza o cadastro de uma nova venda.
        
        Coleta os itens da venda, opcionalmente o cliente e a forma de pagamento,
        e envia os dados para o controlador de vendas.
        """
        super().show_title("Cadastro de Venda")

        venda = Venda(usuario=UserSession.get_logged_user())
        
        items = []
        while True:
            print(colored("\nDigite os dados do produto", 'blue', attrs=['bold']))
            nome_produto = input(colored("Nome do produto: ", 'green'))

            produto = self.produto_controller.buscar_por_nome(nome_produto)
            if produto is None:
                print(colored("Produto não encontrado! Tente novamente.", 'red'))
                continue
            
            quantidade = get_int(
                msg="Informe a quantidade: ",
                min=1,
                max=produto.quantidade,
                max_msg="Quantidade informada excede a quantidade em estoque do produto"
            )
            desconto = get_float(
                msg="\nInforme o desconto (digite 0 se não houver): ",
                min=0.0,
                max=100.0
            )

            items.append(Item(produto=produto, quantidade=quantidade, desconto=desconto, venda=venda))

            print(colored("\nDeseja adicionar mais produtos?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)
            if opcao == 0:
                break

        venda.items = items
        
        cliente = None
        while True:
            print(colored("\nDeseja informar um cliente?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)
            if opcao == 0:
                break

            cpf_cliente = input(colored("Digite o CPF do cliente: ", 'green')).rstrip()
            cliente = self.cliente_controller.buscar_por_cpf(cpf_cliente)
            if cliente is None:
                print(colored("Cliente não encontrado! Tente novamente.", 'red'))
                continue
            else:
                break

        venda.cliente = cliente
        
        formas_dict = self.get_dict_formas_pagamento()
        self.mostrar_formas_pagamento(formas_dict)
        opcao_pagamento = get_int("Selecione a forma de pagamento: ", min=0, max=len(formas_dict) - 1)
        venda.forma_pagamento = formas_dict[opcao_pagamento]

        try:
            is_venda_cadastrada = self.venda_controller.cadastrar_venda(venda)
        except Exception as e:
            print(colored(f"\nErro: {e}\n", 'red'))
            print(colored("Ocorreu um erro inesperado ao cadastrar a venda.", 'red'))
            return

        if is_venda_cadastrada:
            print(colored("\nVenda cadastrada com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao cadastrar a venda.", 'red', attrs=['bold']))

    def get_dict_formas_pagamento(self):
        """
        Cria e retorna um dicionário indexado das formas de pagamento disponíveis.
        
        :return: Dicionário onde a chave é o índice e o valor é o objeto forma de pagamento.
        """
        formas = self.forma_pagamento_controller.find_all()
        dict_formas = {}
        for i in range(len(formas)):
            dict_formas[i] = formas[i]
        return dict_formas

    def mostrar_formas_pagamento(self, formas_dict: dict):
        """
        Exibe as formas de pagamento disponíveis para seleção.

        :param formas_dict: Dicionário contendo as formas de pagamento.
        """
        print("=== Formas de Pagamento ===")
        for i in range(len(formas_dict)):
            print(colored(f"[{i}] {formas_dict[i].nome}", 'light_blue', attrs=['bold']))

    def remover(self):
        """
        Remove uma venda a partir do ID informado.
        
        Permite a remoção de múltiplas vendas.
        """
        print(colored("=" * 40, 'cyan'))
        print(colored("    Deletar Venda", 'yellow', attrs=['bold']))
        print(colored("=" * 40, 'cyan'))

        while True:
            id_venda = get_int(msg="Informe o id da venda: ", min=1)

            is_success = self.venda_controller.delete(id_venda)
            if is_success:
                print(colored("\nVenda removida com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao deletar a venda.", 'red', attrs=['bold']))

            print(colored("\nDeseja deletar mais vendas?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)
            if opcao == 0:
                break

    def listar(self):
        """
        Exibe a lista de vendas.
        
        (Nota: neste exemplo, o método chama find_all() do controlador de formas de pagamento,
        o que pode não ser o comportamento esperado para listar vendas.)
        """
        super().show_title("Lista de Vendas")
        vendas = self.venda_controller.find_all()
        for venda in vendas:
            print(venda)
