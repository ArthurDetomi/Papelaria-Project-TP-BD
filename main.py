from persistence.UsuarioDao import UsuarioDao
from model.Usuario import Usuario
from view.CategoriaView import exibirMenuCategoria
from view.FormaPagamentoView import exibirMenuFormaPagamento
from controller.CategoriaController import CategoriaController
from controller.FormaPagamentoController import FormaPagamentoController

def opcaomenu():
    print("\nGerenciar:")
    print("[0] Produtos")
    print("[1] Vendas")
    print("[2] Usuários")
    print("[3] Categorias")
    print("[4] Formas de pagamento")
    print("[5] Clientes")
    print("[6] Sair")
    
    opcao = input("Selecione uma opção: ")
    return opcao

def menu_categorias():
    categoriacontroller = CategoriaController()
    
    while True:
        opcaocategoria = exibirMenuCategoria()
        
        if opcaocategoria == "0":
            break 
        elif opcaocategoria == "1":
            categoriacontroller.CadastrarCategoria()
        elif opcaocategoria == "2":
            categoriacontroller.AtualizarCategoria()
        elif opcaocategoria == "3":
            categoriacontroller.DeletarCategoria()
        elif opcaocategoria == "4":
            categoriacontroller.ListarCategoria()
        else:
            print("Opção inválida! Tente novamente.")

def menu_formas_pagamento():
    formapagamentocontroller = FormaPagamentoController()
    
    while True:
        opcaoformapagamento = exibirMenuFormaPagamento()
        
        if opcaoformapagamento == "0":
            break  
        elif opcaoformapagamento == "1":
            formapagamentocontroller.CadastrarFormaPagamento()
        elif opcaoformapagamento == "2":
            formapagamentocontroller.AtualizarFormaPagamento()
        elif opcaoformapagamento == "3":
            formapagamentocontroller.DeletarFormaPagamento()
        elif opcaoformapagamento == "4":
            formapagamentocontroller.ListarFormaPagamento()
        else:
            print("Opção inválida! Tente novamente.")
       

def main():
    while True:
        opcao = opcaomenu()

        if opcao == "0":
            print("Você escolheu: Produtos")
        elif opcao == "1":
            print("Você escolheu: Vendas")
        elif opcao == "2":
            print("Você escolheu: Usuários")
        elif opcao == "3":
            menu_categorias()  
        elif opcao == "4":
            menu_formas_pagamento() 
        elif opcao == "5":
            print("Você escolheu: Clientes")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
