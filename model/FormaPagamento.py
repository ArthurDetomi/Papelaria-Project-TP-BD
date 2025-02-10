class FormaPagamento:
    def __init__(self, id=None,  nome=None, cadastrado=None, editado=None):
        self.id = id
        self.nome = nome
        self.cadastrado = cadastrado
        self.editado = editado
    
    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Forma de pagamento: {self.nome}\n"
            f"Data de cadastro: {self.cadastrado}\n"
            f"Ultima modificacao: {self.editado}"
        )
