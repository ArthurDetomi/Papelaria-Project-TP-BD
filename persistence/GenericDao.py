"""Módulo GenericDao.

Contém a classe GenericDao, que define a interface para as operações CRUD
(genéricas) que devem ser implementadas pelos DAOs.
"""


class GenericDao:
    """Interface para operações CRUD genéricas."""

    def save(self, entity):
        """
        Salva uma entidade no banco de dados.
        Deve ser implementado pelas classes derivadas.
        """
        raise NotImplementedError()

    def find_by_id(self, id):
        """
        Recupera uma entidade com base no seu ID.
        Deve ser implementado pelas classes derivadas.
        """
        raise NotImplementedError()

    def find_all(self):
        """
        Recupera todas as entidades.
        Deve ser implementado pelas classes derivadas.
        """
        raise NotImplementedError()

    def delete(self, id):
        """
        Remove uma entidade com base no seu ID.
        Deve ser implementado pelas classes derivadas.
        """
        raise NotImplementedError()

    def update(self, entity):
        """
        Atualiza uma entidade existente.
        Deve ser implementado pelas classes derivadas.
        """
        raise NotImplementedError()
