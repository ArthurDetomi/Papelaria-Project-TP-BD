from persistence.Database import Database
from model.Usuario import Usuario
from persistence.GenericDao import GenericDao

class UsuarioDao(GenericDao):
    
    def find_all(self):
        with Database() as db:
            result = db.query("SELECT * FROM usuario", fetch=True)
        
        users = []
        
        for data in result:
            id_, login, senha, cpf, cadastrado, editado = data
            
            user = Usuario(id=id_, login=login, senha=senha, cpf=cpf, cadastrado=cadastrado, editado=editado)
            
            users.append(user)
            
        
        return users

    def find_by_id(self, id):        
        with Database() as db:
            result = db.query("SELECT * FROM usuario WHERE id = %s", params=(id,), fetch_one=True)
        
        if result is None:
            return None
        
        id_, login, senha, cpf, cadastrado, editado = result
        
        return Usuario(id=id_, login=login, senha=senha, cpf=cpf, cadastrado=cadastrado, editado=editado)
    
    def save(self, usuario : Usuario):
        with Database() as db:
            result = db.query("INSERT INTO usuario (login, senha, cpf) values (%s, %s, %s)", (usuario.login, usuario.senha, usuario.cpf,))
        return result
    
    def delete(self, id):
        with Database() as db:
            result = db.query("DELETE FROM usuario WHERE id = %s", (id,))
        return result
    
    def update(self, usuario : Usuario):
        with Database() as db:
            result = db.query("UPDATE usuario SET login=%s, senha=%s, cpf=%s WHERE id = %s", (usuario.login,usuario.senha,usuario.id,))
        return result
    
            
        

    
    