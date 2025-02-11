from service.UserSession import UserSession

from model.Usuario import Usuario
from persistence.UsuarioDao import UsuarioDao

from datetime import datetime

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
        
        return  self.usuario_dao.save(usuario)

    def atualizar_usuario(self, id, login, senha, cpf):
        usuario = Usuario(id=id, login=login, senha=senha, cpf=cpf)
    
        usuario.login = login or usuario.login
        usuario.senha = senha or usuario.senha
        usuario.cpf = cpf or usuario.cpf
        usuario.editado = datetime.now()
        
        return self.usuario_dao.update(usuario)

    def deletar_usuario(self, id):
        return self.usuario_dao.delete(id)
    
    def find_by_id(self, id):
        return self.usuario_dao.find_by_id(id)

    def listar_usuarios(self):
        usuarios = self.usuario_dao.find_all()

        return usuarios
