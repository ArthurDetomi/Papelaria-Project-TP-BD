from persistence.Database import Database
from model.Cliente import Cliente
from persistence.GenericDao import GenericDao

class ClienteDao(GenericDao):

    def find_all(self):
        """Retorna todos os clientes do banco de dados."""
        with Database() as db:
            result = db.query("SELECT * FROM cliente", fetch=True)

        clientes = []
        for data in result:
            id_, nome, cpf, telefone, cadastrado, editado = data
            clientes.append(Cliente(id=id_, nome=nome, cpf=cpf, telefone=telefone, cadastrado=cadastrado, editado=editado))

        return clientes

    def find_by_id(self, id):
        """Busca um cliente pelo ID."""
        with Database() as db:
            result = db.query("SELECT * FROM cliente WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cpf, telefone, cadastrado, editado = result
        return Cliente(id=id_, nome=nome, cpf=cpf, telefone=telefone, cadastrado=cadastrado, editado=editado)

    def save(self, cliente: Cliente):
        """Insere um novo cliente no banco de dados."""
        with Database() as db:
            result = db.query(
                "INSERT INTO cliente (nome, cpf, telefone) VALUES (%s, %s, %s) RETURNING id",
                (cliente.nome, cliente.cpf, cliente.telefone),
                fetch_one=True
            )
        return result['id'] if result else None

    def update(self, cliente: Cliente):
        """Atualiza um cliente existente no banco de dados."""
        with Database() as db:
            result = db.query(
                "UPDATE cliente SET nome=%s, cpf=%s, telefone=%s, editado=NOW() WHERE id = %s",
                (cliente.nome, cliente.cpf, cliente.telefone, cliente.id)
            )
        return result

    def delete(self, id):
        """Deleta um cliente do banco de dados."""
        with Database() as db:
            result = db.query("DELETE FROM cliente WHERE id = %s", (id,))
        return result
