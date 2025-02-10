from view.MenuEntity import MenuEntity
from termcolor import colored

from model.Item import Item
from model.Venda import Venda

from service.UserSession import UserSession

from controller.VendaController import VendaController
from controller.ProdutoController import ProdutoController
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



    def showTitle(self):
        print(colored("=====================================", 'cyan'))
        print(colored(f"    Vendas", 'yellow', attrs=['bold']))
        print(colored("=====================================", 'cyan'))

    def cadastrar(self):
        print("====Cadastro")

        venda = Venda(usuario=UserSession.getLoggedUser())

        # Coletar itens da venda
        items = []
        while True:
            nome_produto = input("Digite o nome do produto:")

            produto = self.produto_controller.buscar_por_nome(nome_produto)

            if produto == None:
                print("Não foi encontrado o produto com o respectivo nome")
                continue

            # E se não tiver em estoque ?
            quantidade = get_int(msg="Informe a quantidade", min=1, max=produto.quantidade, max_msg="Quantidade informada excede a quantidade em estoque do produto")

            desconto = get_float(msg="Informe o desconto, caso não tenha basta digitar 0:", min=0.0, max=100.0)

            items.append(Item(produto=produto, quantidade=quantidade, desconto=desconto))

            print("Deseja adicionar mais produtos a venda [0]Não[1]Sim")

            opcao = get_int(msg="Selecione:", min=0, max=1)

            if opcao == 0:
                break
            else:
                continue

        venda.items = items

        # Coletar cliente que realizou a venda
        cliente = None

        while True:
            print("Deseja informar o cliente [0]Não[1]Sim")
            opcao = get_int("Selecione:", min=0, max=1)

            if opcao == 0:
                break

            cpf_cliente = input("Digite o cpf do cliente:")

            cliente = self.cliente_controller.buscar_por_cpf(cpf_cliente)

            if cliente == None:
                print("Não foi encontrado cliente com o respectivo cpf")
                continue
            else:
                break

        venda.cliente = cliente

        # Coletar forma de pagamento da venda
        forma_pagamentos_dict = self.get_dict_formas_pagamento()

        self.mostrar_formas_pagamento(formas_pagamentos=forma_pagamentos_dict)

        forma_pagamento_selected = None

        opcao_pagamento = get_int("Selecione a forma de pagamento", min=0, max=len(forma_pagamentos_dict))

        forma_pagamento_selected = forma_pagamentos_dict[opcao_pagamento]

        venda.forma_pagamento = forma_pagamento_selected

        is_venda_cadastrada = False

        try:
            is_venda_cadastrada = VendaController.cadastrarVenda(venda)
        except Exception as e:
            print("Ocorreu um erro inesperado ao cadastrar venda!")

        if is_venda_cadastrada:
            print("Venda cadastrada com sucesso!")
        else:
            print("Falha ao cadastrar venda")


    def get_dict_formas_pagamento(self):
        return {}

    def mostrar_formas_pagamento(self, formas_pagamentos):
        pass


















    def remover(self):
        pass

    def listar(self):
        pass
