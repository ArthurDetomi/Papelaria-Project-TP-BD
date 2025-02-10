from termcolor import colored

class Venda:
    def __init__(self, id=None, usuario=None, items=[], cliente=None, forma_pagamento=None, total=None, cadastrado=None):
        self.id = id
        self.usuario = usuario
        self.forma_pagamento = forma_pagamento
        self.cliente = cliente
        self.total = total
        self.cadastrado = cadastrado
        self.items = items

    def prepararEntidadeParaCadastro(self):
        valor_total = 0

        for item in self.items:
            valor_total += item.valor

        self.total = valor_total

    def __str__(self):
        return (
            f"{colored('ID Venda:', 'cyan')} {self.id} | "
            f"{colored('Usuario:', 'yellow')} {self.usuario.login} | "
            f"{colored('Cliente:', 'green')} {self.cliente.nome if self.cliente else 'Não informado'} | "
            f"{colored('Forma Pagamento:', 'blue')} {self.forma_pagamento.nome if self.forma_pagamento else 'Não informado'} | "
            f"{colored('Total:', 'magenta')} {self.total if self.total else 'Não calculado'}"
            f"{colored('Cadastrado:', 'green')} {self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'} | "
        )
