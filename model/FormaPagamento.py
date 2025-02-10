from termcolor import colored

class FormaPagamento:
    def __init__(self, id=None,  nome=None, cadastrado=None, editado=None):
        self.id = id
        self.nome = nome
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        return (
            f"{colored('ID:', 'cyan')} {self.id} | "
            f"{colored('Nome:', 'yellow')} {self.nome} | "
            f"{colored('Cadastrado:', 'green')} {self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
            f"{colored('Editado:', 'blue')} {self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )
