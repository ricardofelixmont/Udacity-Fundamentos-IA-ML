#!/usr/bin/env python3
# coding: utf-8
# Armazenamento de filmes
# Abaixo temos a lista de dicionários que irá armazenar os filmes:
import os
import csv

# Lista onde são armazendos os filmes em memória
filmes = []

# Abrindo o arquivo csv onde estão armazenados os filmes
with open('filmes.csv', 'r') as arquivo:
    dict_filmes = csv.DictReader(arquivo,delimiter=',')
    for filme in dict_filmes:
        filmes.append(filme)

# Fuções para manipular dos filmes
def novo_filme(titulo, ano, diretor='desconhecido'):
    filmes.append({'titulo':titulo, 'ano':ano, 'diretor':diretor})
    with open('filmes.csv', 'a+') as filme:
        fieldnames = ['titulo', 'ano', 'diretor']
        writer = csv.DictWriter(filme, fieldnames=fieldnames)
        writer.writerow({'titulo': titulo, 'ano': ano, 'diretor':diretor})
    return 'Filme adicionado com sucesso...'

def procurar_filmes_ano(ano):
    for filme in filmes:
        if filme['ano'] == ano:
            return filme

def procurar_filmes_titulo(titulo):
    for filme in filmes:
        if filme['titulo'] == titulo:
            return filme
def procurar_filmes_diretor(diretor):
    for filme in filmes:
        if filme['diretor'] == diretor:
            return filme
def mostrar_todos():
    print('LISTA DE FILMES')
    for filme in filmes:
        print(f'{"="*7} DADOS DO FILME {"="*7}\nTitulo: {filme["titulo"]}\nAno: {filme["ano"]}\nDiretor: {filme["diretor"]}\n{"="*15}')
        

# MENU
print('-='*15)
print('MENU')
print('-='*15)

opcao = 0
while opcao not in [6]:
    titulo = ''
    ano = 0
    diretor = ''
    opcao = int(input('[1] - Adicionar novo filme:\n[2] - Pesquisar por titulo:\n[3] - Pesquisar por autor:\n[4] - Mostrar todos:\n[5] - Pesquisar por ano:\n[6] - Sair\nO que você deseja fazer? '))
    os.system('clear')
    if opcao == 6:
        break
    if opcao == 1:
        titulo = str(input('Digite o nome do filme: '))
        ano = int(input('Digite o ano de lançamento: '))
        diretor = str(input('Digite o nome do diretor: '))

        novo_filme(titulo, ano, diretor)
        filme = procurar_filmes_titulo(titulo)
        print(f'{"="*7} DADOS DO FILME {"="*7}\nTitulo: {filme["titulo"]}\nAno: {filme["ano"]}\nDiretor: {filme["diretor"]}\n{"="*15}')

    elif opcao == 2:
        titulo = str(input('Digite o nome do filme: '))
        print(titulo)
        filme = procurar_filmes_titulo(titulo)
        print(f'{"="*7} DADOS DO FILME {"="*7}\nTitulo: {filme["titulo"]}\nAno: {filme["ano"]}\nDiretor: {filme["diretor"]}\n{"="*15}')
    elif opcao == 3:
        diretor = str(input('Digite o nome do Diretor: '))

        filme = procurar_filmes_diretor(diretor)
        print(f'{"="*7} DADOS DO FILME {"="*7}\nTitulo: {filme["titulo"]}\nAno: {filme["ano"]}\nDiretor: {filme["diretor"]}\n{"="*15}')
    elif opcao == 4:
        mostrar_todos()
    elif opcao == 5:
        ano = int(input('Digite o ano de lançamento: '))
        filme = procurar_filmes_ano(ano)
        print(f'{"="*7} DADOS DO FILME {"="*7}\nTitulo: {filme["titulo"]}\nAno: {filme["ano"]}\nDiretor: {filme["diretor"]}\n{"="*15}')
    else:
        print('Opção inválida, por favor tente novamente...')
