from model.Categoria import Categoria
from persistence.CategoriaDao import CategoriaDao
from datetime import datetime

class CategoriaController:
    def __init__(self):
        self.categoria = CategoriaDao()

    def CadastrarCategoria(self):
        print("\n=== Cadastramento de categoria ===")
        nome = input("Categoria: ")

        if nome == "":
            print("Erro: Categoria invalida!")
            return
        
        cadastrado = datetime.now()

        categoria = Categoria(nome=nome, cadastrado=cadastrado, editado=None)
        self.categoria.save(categoria)

        print("Categoria cadastrada com sucesso!")
    
    def AtualizarCategoria(self):
        print("\n=== Atualizar categoria ===")
        
        id = input("ID da categoria: ")
        categoria = self.categoria.find_by_id(id)

        if categoria:
            print(f"Categoria: {categoria.nome}")
            nome = input("Nova categoria: ")
            if nome != "":
                categoria.editado = datetime.now()
                categoria.nome = nome

            else:
                categoria.nome = categoria.nome
            
            self.categoria.update(categoria)

            print("Categoria atualizada com sucesso!")
        else:
            print("Categoria nao encontrada.")

    def DeletarCategoria(self):
        print("\n=== Deletar categoria ===")
        id = input("ID da categoria: ")

        categoria = self.categoria.find_by_id(id)

        if categoria:
            self.categoria.delete(id)
            print("Categoria deletada com sucesso!")
        else:
            print("Categoria nao encontrada.")


    def ListarCategoria(self):
        print("\n=== Listar categorias ===")
        categoria = self.categoria.find_all()

        if categoria:
            categoriaordenado = sorted(categoria, key=lambda x: x.id)
            for categorias in categoriaordenado:
                print(f"ID: {categorias.id}\nNome: {categorias.nome}\n"
                        f"Data e hora de cadastro: {categorias.cadastrado}\n"
                            f"Data e hora da ultima modificação: {categorias.editado}")
        else:
            print("Nenhuma categoria foi cadastrada.")