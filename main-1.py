import csv  # importa o módulo para trabalhar com arquivos CSV

ARQUIVO = 'livros.csv'  # nome do arquivo onde o catálogo será salvo

livros = []  # lista global que vai guardar todos os livros cadastrados

def cadastro_livros(titulo, autor, codigo, ano, status="disponível"):  # função para cadastrar um livro, com status padrão "disponível"
    livro = {"titulo":titulo,"autor":autor,"codigo":codigo,"ano":ano,"status":status}  # monta o dicionário do livro com os dados recebidos
    livros.append(livro)  # adiciona o dicionário na lista global de livros
