from persistence.FormaPagamentoDao import FormaPagamentoDao

class FormaPagamentoController:

    def __init__(self):
        self.forma_pagamento_dao = FormaPagamentoDao()

    def find_all(self):
        return self.forma_pagamento_dao.find_all()

