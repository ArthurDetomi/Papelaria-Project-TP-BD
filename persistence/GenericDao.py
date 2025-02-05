class GenericDao:
    def save(self, entity):
        raise NotImplementedError()
    
    def find_by_id(self, id):
        raise NotImplementedError()
    
    def find_all(self, id):
        raise NotImplementedError()

    def delete(self, id):
        raise NotImplementedError()