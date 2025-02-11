"""Módulo MenuUsuario.

Fornece a interface de menu para o gerenciamento de usuários, permitindo o
cadastro, listagem, remoção e atualização de usuários.
"""

from view.MenuEntity import MenuEntity
from controller.UsuarioController import UsuarioController
from termcolor import colored


class MenuUsuario(MenuEntity):
    """Menu interativo para operações relacionadas a usuários."""

    def __init__(self):
        super().__init__()
        self.usuario_controller = UsuarioController()

    def show_title(self, title="Usuários"):
        """Exibe o título do menu de usuários."""
        super().show_title(title)

    def cadastrar(self):
        """
        Realiza o cadastro de um novo usuário.
        
        Solicita as credenciais necessárias (login, senha e CPF) e envia para o controlador.
        """
        super().show_title("Cadastrar Usuário")
        print(colored("=== Preencha as credenciais ===\n", 'blue'))

        login = input(colored("Login: ", 'green'))
        senha = input(colored("Senha: ", 'green'))
        cpf = input(colored("CPF: ", 'green'))

        is_usuario_cadastrado = self.usuario_controller.cadastrar_usuario(
            login=login, senha=senha, cpf=cpf
        )

        if is_usuario_cadastrado:
            print(colored("\nUsuário cadastrado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao cadastrar o usuário.", 'red', attrs=['bold']))

    def listar(self):
        """
        Lista todos os usuários cadastrados.
        """
        super().show_title("Lista de Usuários")

        usuarios = self.usuario_controller.listar_usuarios()
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print(self.get_error_message("Nenhum usuário cadastrado"))

    def remover(self):
        """
        Remove um usuário a partir do ID informado.
        """
        super().show_title("Deletar Usuário")

        id_usuario = input(self.get_success_message("ID do usuário: "))
        usuario = self.usuario_controller.find_by_id(id_usuario)

        if usuario is None:
            print(self.get_error_message("\nUsuário não encontrado."))
            return

        is_usuario_deletado = self.usuario_controller.deletar_usuario(id_usuario)
        if is_usuario_deletado:
            print(colored("\nUsuário deletado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao deletar o usuário.", 'red', attrs=['bold']))

    def atualizar(self):
        """
        Atualiza os dados de um usuário existente.
        
        Solicita novos valores para login, senha e CPF, mantendo os valores atuais se
        nenhum novo valor for informado.
        """
        super().show_title("Atualizar Usuário")

        id_usuario = int(input(self.get_success_message("ID do usuário: ")))
        novo_login = input(self.get_success_message("Novo Login (deixe em branco para manter o atual): "))
        nova_senha = input(self.get_success_message("Nova Senha (deixe em branco para manter o atual): "))
        novo_cpf = input(self.get_success_message("Novo CPF (deixe em branco para manter o atual): "))

        usuario = self.usuario_controller.find_by_id(id_usuario)
        if usuario is None:
            print(self.get_error_message("\nUsuário não encontrado."))
            return

        is_usuario_atualizado = self.usuario_controller.atualizar_usuario(
            id=id_usuario, login=novo_login, senha=nova_senha, cpf=novo_cpf
        )

        if is_usuario_atualizado:
            print(colored("\nUsuário atualizado com sucesso!", 'green', attrs=['bold']))
        else:
            print(colored("\nFalha ao atualizar o usuário.", 'red', attrs=['bold']))

    def show_options(self):
        """Exibe as opções disponíveis no menu de usuários."""
        print(colored("[0] Voltar", 'red', attrs=['bold']))
        print(colored("[1] Cadastrar", 'green'))
        print(colored("[2] Visualizar", 'green'))
        print(colored("[3] Remover", 'green'))
        print(colored("[4] Atualizar", 'green'))

    def run_option(self, option: int):
        """
        Executa a opção selecionada no menu de usuários.

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
