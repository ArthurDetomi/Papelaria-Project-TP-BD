from persistence.UsuarioDao import UsuarioDao
from model.Usuario import Usuario

def main():
    dao = UsuarioDao()
    
    usuario = Usuario(login="teste_login", cpf="123-123-123-30", senha="123")

    if dao.save(usuario):
        print("Usuario 1 cadastrado")
        
    usuario2 = Usuario(login="teste_login2", cpf="123-123-123-31", senha="123")

    if dao.save(usuario2):
        print("Usuario 2 cadastrado")
    
    users = dao.find_all()
    print(users)

    usuario = dao.find_by_id(1)
    print(usuario)
    print(dao.find_by_id(12))
    
    
    if dao.delete(17):
        print("Usuario 2 deletado")
    #else:
        print("não deletou")
    
    usuario.login = "teste_login__"
    if (dao.update(usuario)):
        print("Usuario atualizado")
    else:
        print("Não atualizou")


if __name__ == "__main__":
    main()