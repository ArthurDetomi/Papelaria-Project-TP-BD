"""Módulo DataBaseConfig.

Contém a classe DatabaseConfig que gerencia as configurações de conexão com o banco de dados.
"""

class DatabaseConfig:
    """Classe para configurar a conexão com o banco de dados.

    Esta classe implementa o padrão singleton para garantir que apenas uma
    instância de configuração seja criada.
    """
    _instancia = None

    def __new__(cls, *args, **kwargs):
        """
        Cria uma nova instância de DatabaseConfig se nenhuma existir.

        :return: Instância única de DatabaseConfig.
        """
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia

    def __init__(self):
        """
        Inicializa a configuração do banco de dados lendo as propriedades do arquivo.
        """
        properties = self.read_properties()
        self.database = properties["database"]
        self.host = properties["host"]
        self.user = properties["user"]
        self.password = properties["password"]
        self.port = properties["port"]

    def read_properties(self):
        """
        Lê as propriedades de configuração do banco de dados a partir do arquivo.

        :return: Dicionário com as propriedades lidas.
        """
        properties = {}
        with open('resources/db.properties', encoding="utf-8") as f:
            for line in f:
                # Divide a linha na chave e no valor
                parts = line.split("=")
                properties[parts[0]] = parts[1].rstrip()
        return properties
