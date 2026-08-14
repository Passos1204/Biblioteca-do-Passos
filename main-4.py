def menu():
    print("Menu")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")
    opcao = int(input("Faça sua escolha: "))

    if opcao == 1:
        titulo = input("Digite o nome do Livro: ")
        autor = input("Digite o nome do Autor: ")
        codigo = input("Digite o código do Livro: ")
        ano = input("Digite o ano do Livro: ")
        cadastro_livros(titulo, autor, codigo, ano)
        salvar_livros()
        print("Livro cadastrado com sucesso!")

    if opcao == 2:
        emprestar_livro()
        salvar_livros()

    if opcao == 3:
        devolver_livro()
        salvar_livros()

    if opcao == 4:
        listar_livros()
        salvar_livros()

    if opcao == 5:
        buscar_livro()
        salvar_livros()

    if opcao == 6:
        ordenar_livros()
        salvar_livros()

    if opcao == 7:
        print("Até logo!")
        return False

    return True

carregar_livros()
while True:
    continuar = menu()
    if continuar is False:
        break
