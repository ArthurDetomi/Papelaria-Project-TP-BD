class Usuario:
    def __init__(self, id = None, login = "", senha="", cpf="", cadastrado=None, editado=None):
        self.id = id
        self.login = login
        self.senha = senha
        self.cpf = cpf
        self.cadastrado = cadastrado
        self.editado = editado
        
    def __str__(self):
        return (f'Usuário(ID: {self.id}, Login: {self.login}, CPF: {self.cpf}, ')    