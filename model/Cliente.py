from termcolor import colored

class Cliente:
    def __init__(self, id=None, nome="", cpf="", telefone=None, cadastrado=None, editado=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        return (
            f"{colored('ID:', 'cyan')} {self.id} | "
            f"{colored('Nome:', 'yellow')} {self.nome} | "
            f"{colored('CPF:', 'green')} {self.cpf} | "
            f"{colored('Telefone:', 'blue')} {self.telefone if self.telefone else 'Não informado'} | "
            f"{colored('Cadastrado:', 'magenta')} {self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
            f"{colored('Editado:', 'red')} {self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )
