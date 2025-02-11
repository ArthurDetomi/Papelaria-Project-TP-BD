from termcolor import colored

class Produto:
    def __init__(self,
            id=None,
            nome=None,
            preco=None,
            categoria=None,
            quantidade=None,
            unidadeMedida=None,
            cadastrado=None,
            editado=None
        ):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade
        self.unidadeMedida = unidadeMedida
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        return f"""
            {colored('ID:', 'cyan')} {colored(self.id, 'yellow')}
            {colored('Produto:', 'cyan')} {colored(self.nome, 'green')}
            {colored('Preço:', 'cyan')} {colored(f'R$ {self.preco:.2f}', 'red')}
            {colored('Estoque:', 'cyan')} {colored(self.quantidade, 'blue')}
            {colored('Cadastrado em:', 'cyan')} {self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'}
            {colored('Editado em:', 'cyan')} {self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}
        """
