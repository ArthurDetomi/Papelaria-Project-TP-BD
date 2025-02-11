from model.Produto import Produto
from model.Categoria import Categoria
from persistence.ProdutoDao import ProdutoDao
from persistence.CategoriaDao import CategoriaDao
from datetime import datetime

from persistence.ProdutoDao import ProdutoDao

class ProdutoController:
    def __init__(self):
        self.produto_dao = ProdutoDao()
        self.categoria_dao = CategoriaDao()

    def buscar_por_nome(self, nome_produto : str) -> Produto:
        return self.produto_dao.find_by_nome(nome_produto)

    def CadastrarProduto(self):
        print("\n=== Cadastrar Produto ===")
        try:
            nome = input("Nome do produto: ")
            preco = float(input("Preço: R$ "))
            quantidade = int(input("Quantidade em estoque: "))
            unidade_medida = input("Unidade de medida (ex: un, kg, m): ")
            
            # Listar categorias disponíveis
            print("\nCategorias disponíveis:")
            categorias = self.categoria_dao.find_all()
            if not categorias:
                print("Nenhuma categoria cadastrada. Cadastre uma categoria primeiro!")
                return
                
            for cat in categorias:
                print(f"ID: {cat.id} | Nome: {cat.nome}")
            
            categoria_id = int(input("\nID da categoria: "))
            categoria = self.categoria_dao.find_by_id(categoria_id)
            
            if not categoria:
                print("Categoria inválida!")
                return

            novo_produto = Produto(
                nome=nome,
                preco=preco,
                categoria=categoria,
                quantidade=quantidade,
                unidadeMedida=unidade_medida
            )

            if self.produto_dao.save(novo_produto):
                print("\nProduto cadastrado com sucesso!")
                print(f"ID gerado: {novo_produto.id}")

        except ValueError:
            print("Erro: Valores numéricos inválidos!")

    def AtualizarProduto(self):
        print("\n=== Atualizar Produto ===")
        try:
            id_produto = int(input("ID do produto: "))
            produto = self.produto_dao.find_by_id(id_produto)
            
            if produto:
                print(f"\nEditando produto: {produto.nome}")
                print("Deixe em branco para manter o valor atual\n")
                
                novo_nome = input(f"Nome atual ({produto.nome}): ") or produto.nome
                novo_preco = input(f"Preço atual (R$ {produto.preco:.2f}): ") or produto.preco
                nova_unidade = input(f"Unidade medida atual ({produto.unidadeMedida}): ") or produto.unidadeMedida
                
                # Listar categorias
                print("\nCategorias disponíveis:")
                categorias = self.categoria_dao.find_all()
                for cat in categorias:
                    print(f"ID: {cat.id} | Nome: {cat.nome}")
                nova_categoria_id = input(f"\nID Categoria atual ({produto.categoria.id}): ") or produto.categoria.id
                
                nova_categoria = self.categoria_dao.find_by_id(int(nova_categoria_id))
                if not nova_categoria:
                    print("Categoria inválida!")
                    return
                
                produto.nome = novo_nome
                produto.preco = float(novo_preco)
                produto.unidadeMedida = nova_unidade
                produto.categoria = nova_categoria
                
                if self.produto_dao.update(produto):
                    print("\nProduto atualizado com sucesso!")
            else:
                print("Produto não encontrado!")
                
        except ValueError:
            print("Erro: Valores inválidos!")

    def deletar(self, id):
        return self.produto_dao.delete(id)


    def listar(self):
        return self.produto_dao.find_all()

    def find_by_id(self, id):
        return self.produto_dao.find_by_id(id)

    def GerenciarEstoque(self, operacao):
        try:
            print("\n=== Comprar Produto ===") if operacao == "comprar" else print("\n=== Vender Produto ===")
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            
            produto = self.produto_dao.find_by_id(id_produto)
            if produto:
                if operacao == "comprar":
                    if self.produto_dao.comprar(id_produto, quantidade):
                        print(f"Estoque atualizado! Novo total: {produto.quantidade + quantidade}")
                elif operacao == "vender":
                    if produto.quantidade >= quantidade:
                        if self.produto_dao.vender(id_produto, quantidade):
                            print(f"Venda registrada! Novo estoque: {produto.quantidade - quantidade}")
                    else:
                        print("Estoque insuficiente!")
            else:
                print("Produto não encontrado!")
                
        except ValueError:
            print("Valores inválidos!")
