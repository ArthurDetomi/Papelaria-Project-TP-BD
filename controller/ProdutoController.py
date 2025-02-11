from model.Produto import Produto
from model.Categoria import Categoria
from persistence.ProdutoDao import ProdutoDao
from persistence.CategoriaDao import CategoriaDao
from datetime import datetime

class ProdutoController:
    def __init__(self):
        self.dao = ProdutoDao()
        self.categoria_dao = CategoriaDao()

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

            if self.dao.save(novo_produto):
                print("\nProduto cadastrado com sucesso!")
                print(f"ID gerado: {novo_produto.id}")

        except ValueError:
            print("Erro: Valores numéricos inválidos!")

    def AtualizarProduto(self):
        print("\n=== Atualizar Produto ===")
        try:
            id_produto = int(input("ID do produto: "))
            produto = self.dao.find_by_id(id_produto)
            
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
                
                if self.dao.update(produto):
                    print("\nProduto atualizado com sucesso!")
            else:
                print("Produto não encontrado!")
                
        except ValueError:
            print("Erro: Valores inválidos!")

    def DeletarProduto(self):
        print("\n=== Deletar Produto ===")
        try:
            id_produto = int(input("ID do produto: "))
            produto = self.dao.find_by_id(id_produto)
            
            if produto:
                confirmacao = input(f"Tem certeza que deseja excluir '{produto.nome}'? (S/N): ").upper()
                if confirmacao == "S":
                    self.dao.delete(id_produto)
                    print("Produto excluído com sucesso!")
            else:
                print("Produto não encontrado!")
                
        except ValueError:
            print("ID inválido!")

    def ListarProdutos(self):
        print("\n=== Lista de Produtos ===")
        produtos = self.dao.find_all()
        
        if produtos:
            for prod in sorted(produtos, key=lambda x: x.id):
                print(f"ID: {prod.id}")
                print(f"Nome: {prod.nome}")
                print(f"Preço: R$ {prod.preco:.2f}")
                print(f"Categoria: {prod.categoria.nome}")
                print(f"Estoque: {prod.quantidade} {prod.unidadeMedida}")
                print(f"Última atualização: {prod.editado or 'Nunca'}\n")
        else:
            print("Nenhum produto cadastrado!")

    def BuscarPorNome(self):
        print("\n=== Buscar Produtos por Nome ===")
        termo = input("Digite o nome ou parte do nome: ")
        resultados = self.dao.buscar_por_nome(termo)
        
        if resultados:
            print("\nResultados encontrados:")
            for prod in resultados:
                print(f"ID: {prod.id} | {prod.nome} | Estoque: {prod.quantidade} {prod.unidadeMedida}")
        else:
            print("Nenhum produto encontrado!")

    def GerenciarEstoque(self, operacao):
        try:
            print("\n=== Comprar Produto ===") if operacao == "comprar" else print("\n=== Vender Produto ===")
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            
            produto = self.dao.find_by_id(id_produto)
            if produto:
                if operacao == "comprar":
                    if self.dao.comprar(id_produto, quantidade):
                        print(f"Estoque atualizado! Novo total: {produto.quantidade + quantidade}")
                elif operacao == "vender":
                    if produto.quantidade >= quantidade:
                        if self.dao.vender(id_produto, quantidade):
                            print(f"Venda registrada! Novo estoque: {produto.quantidade - quantidade}")
                    else:
                        print("Estoque insuficiente!")
            else:
                print("Produto não encontrado!")
                
        except ValueError:
            print("Valores inválidos!")