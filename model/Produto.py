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
            ID: {self.id}
            Produto:{self.nome}
            Preço: {self.preco}
            Estoque: {self.quantidade}
        """
