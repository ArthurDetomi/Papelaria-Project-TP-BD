from persistence.FormaPagamentoDao import FormaPagamentoDao

from model.FormaPagamento import FormaPagamento

from datetime import datetime

class FormaPagamentoController:

    def __init__(self):
        self.forma_pagamento_dao = FormaPagamentoDao()

    def find_all(self):
        return self.forma_pagamento_dao.find_all()

    def cadastrar(self, nome : str):
        formapagamento = FormaPagamento(nome=nome)

        return self.forma_pagamento_dao.save(formapagamento)

    def find_by_id(self, id):
        return self.forma_pagamento_dao.find_by_id(id)

    def atualizar(self, forma_pagamento : FormaPagamento):
        return self.forma_pagamento_dao.update(forma_pagamento)

    def deletar(self, id):
        return self.forma_pagamento_dao.delete(id)

