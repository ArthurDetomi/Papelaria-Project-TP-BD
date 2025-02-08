class Cliente:
    def __init__(self, id=None, nome="", cpf="", telefone=None, cadastrado=None, editado=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cadastrado = cadastrado
        self.editado = editado

    def __str__(self):
        return (f"Cliente(ID: {self.id}, Nome: {self.nome}, CPF: {self.cpf}, "
                f"Telefone: {self.telefone}, Cadastrado: {self.cadastrado}, Editado: {self.editado})")