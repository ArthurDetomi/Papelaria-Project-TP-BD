class DatabaseConfig:
    _instancia = None
    
    def __init__(self): 
        properties = self.read_properties()
        self.database = properties["database"]
        self.host = properties["host"]
        self.user = properties["user"]
        self.password = properties["password"]
        self.port = properties["port"]
        
    def read_properties(self):
        properties = {}
        with open('resources/db.properties', encoding="utf-8") as f:
            for line in f:
                str = line.split("=")
                properties[str[0]] = str[1].rstrip("\n")
                print(properties)
            
        return properties 
            
        
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia