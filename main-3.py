def listar_livros():  # função que exibe todos os livros cadastrados
    print("Lista de livros cadastrados:")  # título da listagem
    for livro in livros:  # percorre cada livro da lista
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Código: {livro['codigo']}, Ano: {livro['ano']}, Status: {livro['status']}")

def emprestar_livro():  # função que registra o empréstimo de um livro
    print("Emprestar livro")
    titulo = input("Digite o título do livro: ")
    for livro in livros:
        if livro["titulo"] == titulo:
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"
                print("Empréstimo registrado")
            else:
                print("Esse livro já está emprestado.")
            return
    print("Livro não encontrado.")

def devolver_livro():  # função que registra a devolução de um livro
    print("Devolver livro")
    titulo = input("Digite o título do livro: ")
    for livro in livros:
        if livro["titulo"] == titulo:
            if livro["status"] == "emprestado":
                livro["status"] = "disponível"
                print("Devolução registrada com sucesso!")
            else:
                print("Esse livro não está emprestado.")
            return
    print("Livro não encontrado.")

def buscar_livro():  # função que busca livros por título ou autor
    print("Buscar livro")
    termo = input("Digite as informações do livro desejado: ")
    encontrou = False
    for livro in livros:
        if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower():
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Código: {livro['codigo']}, Ano: {livro['ano']}, Status: {livro['status']}")
            encontrou = True
    if not encontrou:
        print("Nenhum livro encontrado com esse termo.")

def ordenar_livros():  # ordena e mostra a lista de livros
    campo = input("Ordenar por (titulo, autor ou ano): ")
    if campo not in ['titulo', 'autor', 'ano']:
        print("Campo inválido!")
        return
    lista = sorted(livros, key=lambda l: l[campo])
    for livro in lista:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Código: {livro['codigo']}, Ano: {livro['ano']}, Status: {livro['status']}")
