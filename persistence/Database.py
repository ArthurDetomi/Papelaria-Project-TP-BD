"""Módulo Database.

Contém a classe Database que gerencia a conexão com o banco de dados PostgreSQL
usando o módulo psycopg2.
"""

import psycopg2
from util.DataBaseConfig import DatabaseConfig


class Database:
    """Classe para gerenciar a conexão e as operações com o banco de dados."""

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados usando as configurações
        definidas em DatabaseConfig.
        """
        db_config = DatabaseConfig()
        self.conn = psycopg2.connect(
            database=db_config.database,
            host=db_config.host,
            user=db_config.user,
            password=db_config.password,
            port=db_config.port
        )
        self.cur = self.conn.cursor()

    def __enter__(self):
        """
        Permite o uso da classe com o gerenciador de contexto.

        :return: Instância da classe Database.
        """
        return self

    def query(self, query, params=None, fetch=False, fetch_one=False):
        """
        Executa uma consulta SQL no banco de dados.

        :param query: Consulta SQL a ser executada.
        :param params: Parâmetros para a consulta SQL.
        :param fetch: Se True, retorna todos os resultados da consulta.
        :param fetch_one: Se True, retorna apenas um resultado da consulta.
        :return: Resultado da consulta ou False em caso de erro.
        """
        try:
            self.cur.execute(query, params)
            if fetch:
                return self.cur.fetchall()
            if fetch_one:
                return self.cur.fetchone()
            self.conn.commit()
            return self.cur.rowcount > 0
        except Exception as e:
            self.conn.rollback()
            return False

    def close(self):
        """
        Fecha o cursor e a conexão com o banco de dados.
        """
        self.cur.close()
        self.conn.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Garante que a conexão seja fechada ao sair do contexto.
        """
        self.close()
