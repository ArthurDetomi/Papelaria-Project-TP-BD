from service.UserSession import UserSession

from model.Usuario import Usuario
from persistence.UsuarioDao import UsuarioDao


class UsuarioController:
    def __init__(self):
        self.usuario_dao = UsuarioDao()

    def realizarLogin(self, login : str, senha : str):
        logged_user = self.usuario_dao.find_by_login_and_senha(login, senha)

        if (logged_user == None):
            return False

        UserSession.setLoggedUser(logged_user)

        return True

    def cadastrar_usuario(self, login, senha, cpf):

        usuario = Usuario(login=login, senha=senha, cpf=cpf)
        if self.usuario_dao.save(usuario):
            print("Usuário cadastrado com sucesso!")
        else:
            print("Usuário já cadastrado!")

    def atualizar_usuario(self, id, login, senha, cpf):

        usuario = self.usuario_dao.find_by_id(id)
        if usuario:
            usuario.login = login or usuario.login
            usuario.senha = senha or usuario.senha
            usuario.cpf = cpf or usuario.cpf
            self.usuario_dao.update(usuario)
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")

    def deletar_usuario(self, id):

        usuario = self.usuario_dao.find_by_id(id)
        if usuario:
            self.usuario_dao.delete(id)
            print("Usuário deletado com sucesso!")
        else:
            print("Usuário não encontrado.")

    def listar_usuarios(self):
        usuarios = self.usuario_dao.find_all()

        return usuarios
