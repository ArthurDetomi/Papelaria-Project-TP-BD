from persistence.FormaPagamentoDao import FormaPagamentoDao

from model.FormaPagamento import FormaPagamento

from datetime import datetime

class FormaPagamentoController:

    def __init__(self):
        self.forma_pagamento_dao = FormaPagamentoDao()

    def find_all(self):
        return self.forma_pagamento_dao.find_all()

    def CadastrarFormaPagamento(self):
        print("\n=== Cadastro da forma de pagamento ===")
        nome = input("Forma de pagamento: ")

        if nome == "":
            print("Erro: Forma de pagamento invalida!")
            return

        cadastrado = datetime.now()

        formapagamento = FormaPagamento(nome=nome, cadastrado=cadastrado, editado=None)
        self.formapagamentodao.save(formapagamento)

        print("Forma de pagamento cadastrada com sucesso!")

    def AtualizarFormaPagamento(self):
        print("\n=== Atualizar forma de pagamento ===")

        id = input("ID da forma de pagamento: ")
        formapagamento = self.formapagamentodao.find_by_id(id)

        if formapagamento:
            print(f"Forma de pagamento: {formapagamento.nome}")
            nome = input("Nova forma de pagamento: ")
            if nome == "":
                formapagamento.nome = formapagamento.nome
            else:
                formapagamento.nome = nome
                editado = datetime.now()
                formapagamento.editado = editado

            self.formapagamentodao.update(formapagamento)
            print("Forma de pagamento atualizada com sucesso!")
        else:
            print("Forma de pagamento nao encontrada.")

    def DeletarFormaPagamento(self):
        print("\n=== Deletar forma de pagamento ===")
        id = input("ID da forma de pagamento: ")

        formapagamento = self.formapagamentodao.find_by_id(id)

        if formapagamento:
            self.formapagamentodao.delete(id)
            print("Forma de pagamento deletada com sucesso!")
        else:
            print("Forma de pagamento nao encontrada.")


    def ListarFormaPagamento(self):
        print("\n=== Listar formas de pagamento ===")
        formapagamento = self.formapagamentodao.find_all()

        if formapagamento:
            for formaspagamento in formapagamento:
                print(f"ID: {formaspagamento.id}\nNome: {formaspagamento.nome}\n"
                        f"Data e hora de cadastro: {formaspagamento.cadastrado}\n"
                            f"Data e hora da ultima modificação: {formaspagamento.editado}")
        else:
            print("Nenhuma forma de pagamento cadastrada.")
