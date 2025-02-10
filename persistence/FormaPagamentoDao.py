from persistence.Database import Database
from model.FormaPagamento import FormaPagamento

class FormaPagamentoDao:

    def find_all(self):
        with Database() as db:
            result = db.query("SELECT * FROM forma_pagamento", fetch=True)

        forma_pagamentos = []

        for data in result:
            id_, nome, cadastrado, editado = data

            fp = FormaPagamento(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)

            forma_pagamentos.append(fp)


        return forma_pagamentos

    def find_by_id(self, id):
        with Database() as db:
            result = db.query("SELECT * FROM forma_pagamento WHERE id = %s", params=(id,), fetch_one=True)

        if result is None:
            return None

        id_, nome, cadastrado, editado = result

        return FormaPagamento(id=id_, nome=nome, cadastrado=cadastrado, editado=editado)

    def save(self, forma_pagamento : FormaPagamento):
        with Database() as db:
            result = db.query("INSERT INTO forma_pagamento (nome) values (%s)", (forma_pagamento.nome,))
        return result

    def delete(self, id):
        with Database() as db:
            result = db.query("DELETE FROM forma_pagamento WHERE id = %s", (id,))
        return result

    def update(self, forma_pagamento : FormaPagamento):
        with Database() as db:
            result = db.query("UPDATE forma_pagamento SET nome=%s, editado=%s WHERE id = %s", (forma_pagamento.nome, forma_pagamento.editado, forma_pagamento.id,))
        return result

