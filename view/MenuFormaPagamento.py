from view.MenuEntity import MenuEntity

from controller.FormaPagamentoController import FormaPagamentoController

from util.StringUtil import is_blank
from util.NumberUtil import get_int

from datetime import datetime

from termcolor import colored

class MenuFormaPagamento(MenuEntity):
    def __init__(self):
        super().__init__()
        self.forma_pagamento_controller = FormaPagamentoController()

    def showTitle(self):
        super().showTitle("Forma de Pagamento")

    def cadastrar(self):
        super().showTitle("Cadastro de Forma de Pagamento")

        while True:
            nome = input(colored("Nome da forma de pagamento: ", 'green'))

            if is_blank(nome):
                print("Erro: Nome de forma de pagamento não pode ser vazio!")
                return

            try:
                is_forma_pagamento_cadastrada = self.forma_pagamento_controller.cadastrar(nome)
            except Exception as e:
                print(colored(f"\nErro: {e}\n", 'red'))
                print(colored("Ocorreu um erro inesperado ao cadastrar a forma de pagamento.", 'red'))

            if is_forma_pagamento_cadastrada:
                print(colored("\nForma de pagamento cadastrada com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao cadastrar a forma de pagamento.", 'red', attrs=['bold']))

            print(colored("\nDeseja cadastrar mais formas de pagamento?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)

            if opcao == 0:
                break

    def remover(self):
        super().showTitle("Deletar Forma de Pagamento")

        while True:
            id_forma_pagemento = get_int(msg="Informe o id da forma de pagamento:", min=1)

            is_success = self.forma_pagamento_controller.deletar(id_forma_pagemento)

            if is_success:
                print(colored("\nForma de pagamento removida com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao deletar a forma de pagamento.", 'red', attrs=['bold']))

            print(colored("\nDeseja deletar mais formas de pagamentos?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)

            if opcao == 0:
                break

    def listar(self):
        super().showTitle("Listar Formas de Pagamentos")

        formapagamentos = self.forma_pagamento_controller.find_all()

        if formapagamentos:
            for formapagamento in formapagamentos:
                print(formapagamento)
        else:
            print(colored("Nenhuma forma de pagamento cadastrada.", 'red', attrs=['bold']))

    def atualizar(self):
        super().showTitle("Atualizar forma de pagamento")

        id = get_int(msg="Informe o id da forma de pagamento:", min=1)

        forma_pagamento = self.forma_pagamento_controller.find_by_id(id)

        if forma_pagamento is not None:
            print(colored(f"\nForma de pagamento: {forma_pagamento.nome}", 'cyan', attrs=['bold']))

            nome = input(colored("\nNova forma de pagamento: ", 'green'))

            if nome == "":
                forma_pagamento.nome = forma_pagamento.nome
            else:
                forma_pagamento.nome = nome
                editado = datetime.now()
                forma_pagamento.editado = editado

            is_forma_pagamento_atualizada = self.forma_pagamento_controller.atualizar(forma_pagamento)

            if is_forma_pagamento_atualizada:
                print(colored("\nForma de pagamento atualizada com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao atualizar a forma de pagamento.", 'red', attrs=['bold']))
        else:
            print(colored("\nForma de pagamento nao encontrada.", 'red', attrs=['bold']))

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





