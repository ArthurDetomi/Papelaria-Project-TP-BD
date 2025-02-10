from model.Usuario import Usuario

class UserSession:
    logged_user = None

    @classmethod
    def setLoggedUser(cls, usuario):
        cls.logged_user = usuario

    @classmethod
    def getLoggedUser(cls) -> Usuario:
        return cls.logged_user
