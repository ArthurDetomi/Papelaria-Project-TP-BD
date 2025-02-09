from persistence.Database import Database
from model.Categoria import Categoria

class CategoriaDao:

    def find_all(self):
        with Database() as db:
            result = db.query("SELECT * FROM categoria", fetch=True)

        categorias = []

        for data in result:
            id_, nome, cadastrado, editado = data

            fp = Categoria(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)

            categorias.append(fp)


        return categorias

    def find_by_id(self, id):
        with Database() as db:
            result = db.query("SELECT * FROM categoria WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cadastrado, editado = result

        return Categoria(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)

    def save(self, categoria : Categoria):
        with Database() as db:
            result = db.query("INSERT INTO categoria (nome, cadastrado, editado) values (%s, %s, %s)", (categoria.nome, categoria.cadastrado, categoria.editado))
        return result

    def delete(self, id):
        with Database() as db:
            result = db.query("DELETE FROM categoria WHERE id = %s", (id,))
        return result

    def update(self, categoria : Categoria):
        with Database() as db:
            result = db.query("UPDATE categoria SET nome=%s, editado=%s WHERE id = %s", (categoria.nome, categoria.editado, categoria.id,))
        return result


