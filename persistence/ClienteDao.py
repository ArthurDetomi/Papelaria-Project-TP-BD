from persistence.Database import Database
from model.Cliente import Cliente

class ClienteDao():

    def find_all(self):
        with Database() as db:
            result = db.query("SELECT * FROM cliente", fetch=True)

        clientes = []

        for data in result:
            id_, nome, cpf, telefone, cadastrado, editado = data

            client = Cliente(id=id_, nome=nome, telefone=telefone, cpf=cpf, cadastrado=cadastrado, editado=editado)

            clientes.append(client)


        return clientes

    def find_by_id(self, id):
        with Database() as db:
            result = db.query("SELECT * FROM cliente WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cpf, telefone, cadastrado, editado = result

        return Cliente(id=id_, nome=nome, telefone=telefone, cpf=cpf, cadastrado=cadastrado, editado=editado)

    def find_by_cpf(self, cpf):
        with Database() as db:
            result = db.query("SELECT * FROM cliente WHERE cpf = %s", params=(cpf,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cpf, telefone, cadastrado, editado = result

        return Cliente(id=id_, nome=nome, telefone=telefone, cpf=cpf, cadastrado=cadastrado, editado=editado)

    def save(self, cliente : Cliente):
        with Database() as db:
            result = db.query("INSERT INTO cliente (nome, cpf, telefone) values (%s, %s, %s)", (cliente.nome, cliente.cpf, cliente.telefone,))
        return result

    def delete(self, id):
        with Database() as db:
            result = db.query("DELETE FROM cliente WHERE id = %s", (id,))
        return result

    def update(self, cliente : Cliente):
        with Database() as db:
            result = db.query("UPDATE cliente SET nome=%s, cpf=%s, telefone=%s WHERE id = %s", (cliente.nome,cliente.cpf,cliente.telefone,cliente.id,))
        return result
