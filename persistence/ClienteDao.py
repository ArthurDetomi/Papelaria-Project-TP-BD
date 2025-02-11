"""Módulo ClienteDao.

Contém a classe ClienteDao, responsável pelas operações de acesso a dados
da entidade Cliente.
"""

from persistence.Database import Database
from model.Cliente import Cliente


class ClienteDao:
    """DAO (Data Access Object) para a entidade Cliente."""

    def find_all(self):
        """
        Recupera todos os clientes do banco de dados.

        :return: Lista de objetos Cliente.
        """
        with Database() as db:
            result = db.query("SELECT * FROM cliente", fetch=True)

        clientes = []
        for data in result:
            id_, nome, cpf, telefone, cadastrado, editado = data
            cliente = Cliente(
                id=id_,
                nome=nome,
                cpf=cpf,
                telefone=telefone,
                cadastrado=cadastrado,
                editado=editado
            )
            clientes.append(cliente)

        return clientes

    def find_by_id(self, id):
        """
        Recupera um cliente com base no seu ID.

        :param id: ID do cliente.
        :return: Objeto Cliente se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query("SELECT * FROM cliente WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cpf, telefone, cadastrado, editado = result
        return Cliente(
            id=id_,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            cadastrado=cadastrado,
            editado=editado
        )

    def find_by_cpf(self, cpf):
        """
        Recupera um cliente com base no CPF.

        :param cpf: CPF do cliente.
        :return: Objeto Cliente se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query("SELECT * FROM cliente WHERE cpf = %s", params=(cpf,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cpf, telefone, cadastrado, editado = result
        return Cliente(
            id=id_,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            cadastrado=cadastrado,
            editado=editado
        )

    def save(self, cliente: Cliente):
        """
        Insere um novo cliente no banco de dados.

        :param cliente: Objeto Cliente a ser salvo.
        :return: Resultado da operação de inserção.
        """
        with Database() as db:
            result = db.query(
                "INSERT INTO cliente (nome, cpf, telefone) VALUES (%s, %s, %s)",
                (cliente.nome, cliente.cpf, cliente.telefone,)
            )
        return result

    def delete(self, id):
        """
        Remove um cliente do banco de dados com base no seu ID.

        :param id: ID do cliente a ser removido.
        :return: Resultado da operação de exclusão.
        """
        with Database() as db:
            result = db.query("DELETE FROM cliente WHERE id = %s", (id,))
        return result

    def update(self, cliente: Cliente):
        """
        Atualiza os dados de um cliente existente.

        :param cliente: Objeto Cliente com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            result = db.query(
                "UPDATE cliente SET nome=%s, cpf=%s, telefone=%s WHERE id = %s",
                (cliente.nome, cliente.cpf, cliente.telefone, cliente.id,)
            )
        return result
