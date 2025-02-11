"""Módulo MenuAbstrato.

Define a classe abstrata MenuAbstrato, que fornece a estrutura base para
menus interativos do sistema.
"""

from termcolor import colored
from util.NumberUtil import get_int


class MenuAbstrato:
    """Classe abstrata para a criação de menus interativos."""

    def show_menu(self):
        """
        Exibe o menu principal, solicitando a opção do usuário e executando
        a ação correspondente.
        """
        while True:
            self.show_title()

            self.show_options()

            option = get_int(msg="Informe sua opção: ", min=0)
            option_selected = self.run_option(option)

            if option_selected == 0:
                print(colored("Fim do programa", 'light_red', attrs=['bold']))
                print(colored("Obrigado por usar o sistema! Até a próxima!", 'green', attrs=['bold']))
                break

    def show_title(self, title=""):
        """
        Exibe o título do menu formatado.

        :param title: Título a ser exibido.
        """
        print(colored("=" * 40, 'cyan'))
        print(colored(f"    {title}", 'yellow', attrs=['bold']))
        print(colored("=" * 40, 'cyan'))

    def get_success_message(self, msg: str) -> str:
        """
        Retorna a mensagem formatada em verde para sucesso.

        :param msg: Mensagem a ser exibida.
        :return: Mensagem formatada.
        """
        return colored(msg, 'green')

    def get_error_message(self, msg: str) -> str:
        """
        Retorna a mensagem formatada em vermelho para erro.

        :param msg: Mensagem a ser exibida.
        :return: Mensagem formatada.
        """
        return colored(msg, 'red')

    def get_blue_message(self, msg: str) -> str:
        """
        Retorna a mensagem formatada em azul.

        :param msg: Mensagem a ser exibida.
        :return: Mensagem formatada.
        """
        return colored(msg, 'blue')

    def run_option(self, option: int):
        """
        Executa a opção selecionada pelo usuário.
        
        Deve ser implementado pelas subclasses.

        :param option: Opção selecionada.
        :raises NotImplementedError: Se não for implementado na subclasse.
        """
        raise NotImplementedError()

    def show_options(self):
        """
        Exibe as opções disponíveis no menu.
        
        Deve ser implementado pelas subclasses.
        """
        raise NotImplementedError()
