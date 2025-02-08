from persistence.Database import Database
from model.Usuario import Usuario
from persistence.GenericDao import GenericDao

class UsuarioDao(GenericDao):

    def find_all(self):
        """Retorna todos os usuários do banco de dados."""
        with Database() as db:
            result = db.query("SELECT * FROM usuario", fetch=True)

        users = []
        for data in result:
            id_, login, senha, cpf, cadastrado, editado = data
            users.append(Usuario(id=id_, login=login, senha=senha, cpf=cpf, cadastrado=cadastrado, editado=editado))

        return users

    def find_by_id(self, id):
        """Busca um usuário pelo ID."""
        with Database() as db:
            result = db.query("SELECT * FROM usuario WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, login, senha, cpf, cadastrado, editado = result
        return Usuario(id=id_, login=login, senha=senha, cpf=cpf, cadastrado=cadastrado, editado=editado)

    def save(self, usuario: Usuario):
        """Insere um novo usuário no banco de dados."""
        with Database() as db:
            result = db.query(
                sql="INSERT INTO usuario (login, senha, cpf) VALUES (%s, %s, %s) RETURNING id",
                params=(usuario.login, usuario.senha, usuario.cpf),
                fetch_one=True
            )
        return result['id'] if result else None

    def update(self, usuario: Usuario):
        """Atualiza um usuário existente no banco de dados."""
        with Database() as db:
            result = db.query(
                "UPDATE usuario SET login=%s, senha=%s, cpf=%s, editado=NOW() WHERE id = %s",
                (usuario.login, usuario.senha, usuario.cpf, usuario.id)
            )
        return result

    def delete(self, id):
        """Deleta um usuário do banco de dados."""
        with Database() as db:
            result = db.query("DELETE FROM usuario WHERE id = %s", (id,))
        return result
