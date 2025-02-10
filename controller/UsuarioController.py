from persistence.UsuarioDao import UsuarioDao
from service.UserSession import UserSession

class UsuarioController:
    def __init__(self):
        self.usuario_dao = UsuarioDao()

    def realizarLogin(self, login : str, senha : str):
        logged_user = self.usuario_dao.find_by_login_and_senha(login, senha)

        if (logged_user == None):
            return False

        UserSession.setLoggedUser(logged_user)

        return True










