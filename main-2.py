def carregar_livros():  # função que lê o arquivo CSV e carrega os livros salvos para a memória
    with open(ARQUIVO,'r',encoding='UTF-8',newline='') as biblioteca:  # abre o arquivo em modo leitura
        cabecalho=["titulo","autor","codigo","ano","status"]  # define os nomes das colunas do CSV
        leitor=csv.DictReader(biblioteca,fieldnames=cabecalho)  # cria o leitor que transforma cada linha do arquivo em dicionário
        for livro in leitor:  # percorre cada linha lida do arquivo
            livros.append(livro)  # adiciona o livro lido na lista global

def salvar_livros():  # função que grava a lista de livros no arquivo CSV
    with open(ARQUIVO,'w',encoding='UTF-8',newline='') as biblioteca:  # abre o arquivo em modo escrita, sobrescrevendo o conteúdo anterior
        cabecalho=["titulo","autor","codigo","ano","status"]  # define os nomes das colunas do CSV
        escritor=csv.DictWriter(biblioteca,fieldnames=cabecalho)  # cria o escritor de CSV
        escritor.writerows(livros)  # escreve todos os livros da lista de uma vez no arquivo
