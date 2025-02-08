from model.Usuario import Usuario
from persistence.UsuarioDao import UsuarioDao

class UsuarioController:
    def __init__(self):
        self.usuario_dao = UsuarioDao()

    def cadastrar_usuario(self):
        print("\n=== Cadastrar Usuário ===")
        login = input("Login: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")

        usuario = Usuario(login=login, senha=senha, cpf=cpf)
        self.usuario_dao.save(usuario)
        print("Usuário cadastrado com sucesso!")

    def atualizar_usuario(self):
        print("\n=== Atualizar Usuário ===")
        id = input("ID do usuário: ")
        usuario = self.usuario_dao.find_by_id(id)

        if usuario:
            print(f"Usuário encontrado: {usuario.login} - {usuario.cpf}")
            login = input("Novo Login (deixe em branco para manter o atual): ") or usuario.login
            senha = input("Nova Senha (deixe em branco para manter a atual): ") or usuario.senha
            cpf = input("Novo CPF (deixe em branco para manter o atual): ") or usuario.cpf

            usuario.login = login
            usuario.senha = senha
            usuario.cpf = cpf
            self.usuario_dao.update(usuario)
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")

    def deletar_usuario(self):
        print("\n=== Deletar Usuário ===")
        id = input("ID do usuário: ")

        usuario = self.usuario_dao.find_by_id(id)
        if usuario:
            self.usuario_dao.delete(id)
            print("Usuário deletado com sucesso!")
        else:
            print("Usuário não encontrado.")

    def listar_usuarios(self):
        print("\n=== Lista de Usuários ===")
        usuarios = self.usuario_dao.find_all()

        if usuarios:
            for usuario in usuarios:
                print(f"ID: {usuario.id}, Login: {usuario.login}, CPF: {usuario.cpf}")
        else:
            print("Nenhum usuário cadastrado.")
