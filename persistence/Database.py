# persistence/Database.py

import psycopg2
from psycopg2.extras import RealDictCursor
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        """Inicializa a conexão com o banco de dados usando as configurações definidas."""
        self.connection = psycopg2.connect(**DATABASE_CONFIG)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def query(self, sql, params=None, fetch=False, fetch_one=False):
        """Executa uma consulta no banco de dados."""
        try:
            self.cursor.execute(sql, params or ())
            if fetch_one:
                return self.cursor.fetchone()
            if fetch:
                return self.cursor.fetchall()
            self.connection.commit()
        except psycopg2.Error as e:
            print(f"Erro ao executar a query: {e}")
            self.connection.rollback()
        return None

    def __enter__(self):
        """Permite o uso de 'with' para gerenciamento seguro da conexão."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Garante o fechamento correto da conexão."""
        self.cursor.close()
        self.connection.close()
