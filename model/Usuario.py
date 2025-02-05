import datetime

class Usuario:
    def __init__(self, id : int, login : str, senha : str, cpf : str, cadastrado : datetime, editado: datetime):
        self.id = id
        self.login = login
        self.senha = senha
        self.cpf = cpf
        self.cadastrado = cadastrado
        self.editado = editado
        
    def __str__(self):
        return (f'Usuário(ID: {self.id}, Login: {self.login}, CPF: {self.cpf}, '
                f'Cadastrado em: {self.cadastrado.strftime("%d/%m/%Y %H:%M:%S")}, '
                f'Última edição em: {self.editado.strftime("%d/%m/%Y %H:%M:%S")})')    