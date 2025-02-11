"""Módulo MenuFormaPagamento.

Fornece a interface de menu para o gerenciamento de formas de pagamento, permitindo
o cadastro, listagem, remoção e atualização.
"""

from view.MenuEntity import MenuEntity
from controller.FormaPagamentoController import FormaPagamentoController
from util.StringUtil import is_blank
from util.NumberUtil import get_int
from datetime import datetime
from termcolor import colored


class MenuFormaPagamento(MenuEntity):
    """Menu interativo para operações relacionadas a formas de pagamento."""

    def __init__(self):
        super().__init__()
        self.forma_pagamento_controller = FormaPagamentoController()

    def show_title(self, title="Forma de Pagamento"):
        """Exibe o título do menu de forma de pagamento."""
        super().show_title(title)

    def cadastrar(self):
        """
        Realiza o cadastro de uma nova forma de pagamento.
        
        Solicita o nome da forma e permite múltiplos cadastros.
        """
        super().show_title("Cadastro de Forma de Pagamento")

        while True:
            nome = input(colored("Nome da forma de pagamento: ", 'green'))

            if is_blank(nome):
                print("Erro: Nome de forma de pagamento não pode ser vazio!")
                return

            try:
                is_forma_cadastrada = self.forma_pagamento_controller.cadastrar(nome)
            except Exception as e:
                print(colored(f"\nErro: {e}\n", 'red'))
                print(colored("Ocorreu um erro inesperado ao cadastrar a forma de pagamento.", 'red'))
                return

            if is_forma_cadastrada:
                print(colored("\nForma de pagamento cadastrada com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao cadastrar a forma de pagamento.", 'red', attrs=['bold']))

            print(colored("\nDeseja cadastrar mais formas de pagamento?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)
            if opcao == 0:
                break

    def remover(self):
        """
        Remove uma forma de pagamento a partir do ID informado.
        
        Permite a remoção de múltiplas formas e exibe mensagens de sucesso ou falha.
        """
        super().show_title("Deletar Forma de Pagamento")

        while True:
            id_forma = get_int(msg="Informe o id da forma de pagamento: ", min=1)

            is_success = self.forma_pagamento_controller.deletar(id_forma)
            if is_success:
                print(colored("\nForma de pagamento removida com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao deletar a forma de pagamento.", 'red', attrs=['bold']))

            print(colored("\nDeseja deletar mais formas de pagamento?", 'cyan'))
            print(colored("[0] Não", 'red'), colored("[1] Sim", 'green'))

            opcao = get_int(msg="\nSelecione: ", min=0, max=1)
            if opcao == 0:
                break

    def listar(self):
        """
        Lista todas as formas de pagamento cadastradas e as exibe na tela.
        """
        super().show_title("Listar Formas de Pagamento")

        formas = self.forma_pagamento_controller.find_all()
        if formas:
            for forma in formas:
                print(forma)
        else:
            print(colored("Nenhuma forma de pagamento cadastrada.", 'red', attrs=['bold']))

    def atualizar(self):
        """
        Atualiza uma forma de pagamento existente, solicitando o novo nome.
        """
        super().show_title("Atualizar Forma de Pagamento")

        id_forma = get_int(msg="Informe o id da forma de pagamento: ", min=1)
        forma = self.forma_pagamento_controller.find_by_id(id_forma)

        if forma is not None:
            print(colored(f"\nForma de pagamento: {forma.nome}", 'cyan', attrs=['bold']))
            novo_nome = input(colored("\nNova forma de pagamento: ", 'green'))

            if novo_nome.strip():
                forma.nome = novo_nome
                forma.editado = datetime.now()

            is_atualizada = self.forma_pagamento_controller.atualizar(forma)
            if is_atualizada:
                print(colored("\nForma de pagamento atualizada com sucesso!", 'green', attrs=['bold']))
            else:
                print(colored("\nFalha ao atualizar a forma de pagamento.", 'red', attrs=['bold']))
        else:
            print(colored("\nForma de pagamento não encontrada.", 'red', attrs=['bold']))

    def show_options(self):
        """Exibe as opções disponíveis no menu de forma de pagamento."""
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))
        print(colored("[4] Atualizar", 'green'))

    def run_option(self, option: int):
        """
        Executa a opção selecionada no menu de forma de pagamento.

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
