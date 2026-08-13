import csv

ARQUIVO = 'livros.csv'

livros = []
def cadastro_livros(titulo, autor, codigo, ano, status= "disponível"):
    livros.append ((titulo, autor, codigo, ano, status))

def menu():
    print("Menu")
    print("1 - Cadastrar livro")
    opcao = int(input("Faça sua escolha: "))
    if opcao == 1:
        titulo = input ()
        autor = input ()
        codigo = input ()
        ano = input ()
        cadastro_livros(titulo, autor, codigo, ano)
        print("Livro cadastrado com sucesso!")

def listar_livros():
    print("Lista de livros cadastrados:")
    for livro in livros:
        print(f"Título: {livro[0]}, Autor: {livro[1]}, Código: {livro[2]}, Ano: {livro[3]}, Status: {livro[4]}")

def emprestar_livro():
    print("Emprestar livro")
    codigo = input("Digite o código do livro: ")
    for livro in livros:
        if livro[2] == codigo:
            livro[4] = "emprestado"
            print("Empréstimo registrado com sucesso!")
            return
    print("Livro não encontrado.")

def devolver_livro():
    print("Devolver livro")
    codigo = input("Digite o código do livro: ")
    for livro in livros:
        if livro[2] == codigo:
            livro[4] = "disponível"
            print("Devolução registrada com sucesso!")
            return
    print("Livro não encontrado.")

def buscar_livro():
    print("Buscar livro")
    termo = input("Digite as informações do livro desejado: ")
    for livro in livros:
        if termo.lower() in livro[0].lower() or termo.lower() in livro[1].lower():
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Código: {livro[2]}, Ano: {livro[3]}, Status: {livro[4]}")

def menu():
    print("Menu")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar listagem")
    print("7 - Sair")
    opcao = int(input("Faça sua escolha: "))

    if opcao == 1:
        titulo = input()
        autor = input()
        codigo = input()
        ano = input()
        cadastro_livros(titulo, autor, codigo, ano)
        print("Livro cadastrado com sucesso!")

    if opcao == 2:
        emprestar_livro()

    if opcao == 3:
        devolver_livro()

    if opcao == 4:
        listar_livros()

    if opcao == 5:
        buscar_livro()

    if opcao == 6:
        ordenar_livros()

    return opcao