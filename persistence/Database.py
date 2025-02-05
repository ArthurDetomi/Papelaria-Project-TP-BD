import psycopg2

from util.DataBaseConfig import DatabaseConfig

class Database:
    def __init__(self):
        db_config = DatabaseConfig()
            
        self.conn = psycopg2.connect(
            database= db_config.database,
            host = db_config.host,
            user = db_config.user,
            password = db_config.password,
            port = db_config.port
        )
        
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self
    
    def query(self, query, params=None, fetch=False, fetch_one=False):
        self.cur.execute(query, params)
        if fetch:
            return self.cur.fetchall()
        if fetch_one:
            return self.cur.fetchone()
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
        
    def __exit__(self,exc_type, exc_value, traceback):
        self.close()