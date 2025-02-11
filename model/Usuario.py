from termcolor import colored

class Usuario:
    def __init__(self, id=None, login="", senha="", cpf="", cadastrado=None, editado=None):
        self.id = id
        self.login = login
        self.senha = senha
        self.cpf = cpf
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        return (
            f"{colored('ID:', 'cyan')} {self.id} | "
            f"{colored('Login:', 'yellow')} {self.login} | "
            f"{colored('CPF:', 'green')} {self.cpf} | "
            f"{colored('Cadastrado:', 'blue')} {self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
            f"{colored('Editado:', 'magenta')} {self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )
