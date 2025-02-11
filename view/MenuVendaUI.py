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
    def __init__(self):
        super().__init__()
        self.venda_controller = VendaController()
        self.produto_controller = ProdutoController()
        self.item_controller = ItemController()
        self.forma_pagamento_controller = FormaPagamentoController()
        self.cliente_controller = ClienteController()

    def showTitle(self):
        super().showTitle("Vendas")

    def cadastrar(self):
        super().showTitle("Cadastro de Venda")

        venda = Venda(usuario=UserSession.getLoggedUser())

        # Coletar itens da venda
        items = []
        while True:
            print(colored("\nDigite os dados do produto", 'blue', attrs=['bold']))
            nome_produto = input(colored("Nome do produto: ", 'green'))

            produto = self.produto_controller.buscar_por_nome(nome_produto)

            if produto == None:
                print(colored("Produto não encontrado! Tente novamente.", 'red'))
                continue

            # E se não tiver em estoque ?
            quantidade = get_int(msg="Informe a quantidade :", min=1, max=produto.quantidade, max_msg="Quantidade informada excede a quantidade em estoque do produto")

            desconto = get_float(msg="\nInforme o desconto, caso não tenha basta digitar [0] :", min=0.0, max=100.0)

            items.append(Item(produto=produto, quantidade=quantidade, desconto=desconto, venda=venda))

            print(colored("\nDeseja adicionar mais produtos?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)

            if opcao == 0:
                break
            else:
                continue

        venda.items = items

        # Coletar cliente que realizou a venda
        cliente = None

        while True:
            print(colored("\nDeseja informar um cliente?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int("\nSelecione: ", min=0, max=1)

            if opcao == 0:
                break

            cpf_cliente = input(colored("Digite o CPF do cliente: ", 'green')).rstrip()

            cliente = self.cliente_controller.buscar_por_cpf(cpf_cliente)

            if cliente == None:
                print(colored("Cliente não encontrado! Tente novamente.", 'red'))
                continue
            else:
                break

        venda.cliente = cliente

        # Coletar forma de pagamento da venda
        forma_pagamentos_dict = self.get_dict_formas_pagamento()

        self.mostrar_formas_pagamento(formas_pagamentos_dict=forma_pagamentos_dict)

        forma_pagamento_selected = None

        opcao_pagamento = get_int("Selecione a forma de pagamento :", min=0, max=len(forma_pagamentos_dict))

        forma_pagamento_selected = forma_pagamentos_dict[opcao_pagamento]

        venda.forma_pagamento = forma_pagamento_selected

        is_venda_cadastrada = False

        try:
            is_venda_cadastrada = self.venda_controller.cadastrar_venda(venda)
        except Exception as e:
            print(colored(f"\nErro: {e}\n", 'red'))
            print(colored("Ocorreu um erro inesperado ao cadastrar a venda.", 'red'))

        if is_venda_cadastrada:
            print(colored("\nVenda cadastrada com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao cadastrar a venda.", 'red', attrs=['bold']))

    def get_dict_formas_pagamento(self):
        formas_pagamentos = self.forma_pagamento_controller.find_all()

        dict = {}

        for i in range(len(formas_pagamentos)):
            dict[i] = formas_pagamentos[i]

        return dict

    def mostrar_formas_pagamento(self, formas_pagamentos_dict = {}):
        print("===Formas pagamentos")
        for i in range(len(formas_pagamentos_dict)):
            print(colored(f"[{i}] {formas_pagamentos_dict[i].nome}", 'light_blue', attrs=['bold']))

    def remover(self):
        print(colored("="*40, 'cyan'))
        print(colored("    Deletar Venda", 'yellow', attrs=['bold']))
        print(colored("="*40, 'cyan'))

        while True:
            id_venda = get_int(msg="Informe o id da venda:", min=1)

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
        super().showTitle("Lista de Vendas")

        vendas = self.venda_controller.find_all()

        for venda in vendas:
            print(venda)


