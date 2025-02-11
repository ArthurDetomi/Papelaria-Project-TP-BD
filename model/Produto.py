"""Módulo Produto.

Contém a classe Produto que representa um produto com seus detalhes, como nome, preço,
categoria, quantidade disponível e unidade de medida.
"""

from termcolor import colored


class Produto:
    """Classe que representa um Produto.

    Atributos:
        id: Identificador único do produto.
        nome: Nome do produto.
        preco: Preço do produto.
        categoria: Categoria à qual o produto pertence.
        quantidade: Quantidade disponível em estoque.
        unidade_medida: Unidade de medida do produto.
        cadastrado: Data/hora de cadastro.
        editado: Data/hora da última edição.
    """

    def __init__(self, id=None, nome=None, preco=None, categoria=None,
                 quantidade=None, unidade_medida=None, cadastrado=None, editado=None):
        """
        Inicializa uma nova instância de Produto.

        :param id: Identificador único do produto.
        :param nome: Nome do produto.
        :param preco: Preço do produto.
        :param categoria: Categoria do produto.
        :param quantidade: Quantidade disponível em estoque.
        :param unidade_medida: Unidade de medida do produto.
        :param cadastrado: Data/hora de cadastro.
        :param editado: Data/hora da última edição.
        """
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade
        self.unidade_medida = unidade_medida
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        """
        Retorna uma representação em string formatada do Produto.

        :return: Representação em string do produto com cores.
        """
        return (
            f"{colored('ID:', 'cyan')} {colored(self.id, 'yellow')}\n"
            f"{colored('Produto:', 'cyan')} {colored(self.nome, 'green')}\n"
            f"{colored('Categoria:', 'cyan')} {colored(self.categoria if self.categoria else 'Não foi carregado', 'magenta')}\n"
            f"{colored('Preço:', 'cyan')} {colored(f'R$ {self.preco:.2f}', 'red')}\n"
            f"{colored('Estoque:', 'cyan')} {colored(self.quantidade, 'blue')}\n"
            f"{colored('Unidade de Medida:', 'cyan')} {colored(self.unidadeMedida if self.unidadeMedida else 'Não informado', 'light_blue')}\n"
            f"{colored('Cadastrado em:', 'cyan')} "
            f"{self.cadastrado.strftime('%d/%m/%Y %H:%M:%S') if self.cadastrado else 'Não informado'}\n"
            f"{colored('Editado em:', 'cyan')} "
            f"{self.editado.strftime('%d/%m/%Y %H:%M:%S') if self.editado else 'Não informado'}"
        )


