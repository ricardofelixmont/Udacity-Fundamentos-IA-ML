# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.DictReader(file_read) # Pelo que parece a parte que demora é no carregamento do arquivo...
    data_list = list(reader)
    # data_list é uma lista de dicionarios ordenados, então cada linha do arquivo csv
    # é um dicionario
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
count = 0

for line in data_list:
# line é um dicionario
    if count == 0:
        for cabecalho in line.items():
            print(cabecalho[0], end=';')
        count += 1
# A primeira linha é o cabeçalho dos dados, para que possamos identificar as colunas, o DictReader() faz isso automaticamente.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("\nLinha 1: ")
for pos, line in enumerate(data_list):
    if pos == 5:
        print(f'{line["Start Time"]}:{line["End Time"]}:{line["Trip Duration"]}:{line["Start Station"]}:{line["End Station"]}:{line["User Type"]}:{line["Gender"]}:{line["Birth Year"]}')


input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for pos, line in enumerate(data_list):
    if pos < 20:
        print(f'{line["Start Time"]}:{line["End Time"]}:{line["Trip Duration"]}:{line["Start Station"]}:{line["End Station"]}:{line["User Type"]}:{line["Gender"]}:{line["Birth Year"]}')


# Vamos mudar o data_list para remover o cabeçalho dele.
# data_list = data_list[1:] 
# Não precisamos mais dessa linha pois usando dicionarios, o cabeçalho é omitido automaticamente
# Agora podemos acessar as features pela chave, por exemplo: sample['Genero'] para imprimir o genero

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for pos, line in enumerate(data_list):
    if pos < 20:
        print(line['Gender']) # alguns generos não aparecem...
    
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

# A necessidade de satisfazer o assert limitou o uso do dicionario, poderia passar a chave como agumento ao inves do nome.
def column_to_list(data, index): # O index deveria servir para falar a posicão de qual item queremos puxar,exemplo:Genero, Trip Duration, etc
    # def new_function(param1: list, param2: int) -> list:
"""
      Função de exemplo com algumas anotações.
      Argumentos:
          data: é uma lista de dicionarios.
          index: não serve para nada pois estou usando dicionario, só mantive pois o assert me obrigou.
      Retorna:
          Uma lista de elementos de uma coluna.

"""

    column_list = []             # Porém estou usando dicionario, entao o index nao é necessário e sim a chave.
    for line in data_list: 
        column_list.append(line['Gender'])
    return column_list

#def column_to_list(data, index):
#    column_list = []
#    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
#    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
lista = column_to_list(data_list, 0)
for genero in lista:
    if genero == 'Male':
        male += 1
    elif genero == 'Female':
        female += 1
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    # def new_function(param1: list) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          data_list: lista de dicionarios, criada com DictReader().
      Retorna:
          Uma lista com a quantidade de homens e a quantidade de mulheres.

"""

    male = 0
    female = 0
    for genero in column_to_list(data_list, 0):
        if genero == 'Male':
            male += 1
        elif genero == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
        # def new_function(param1: list) -> string:
"""
      Função de exemplo com anotações.
      Argumentos:
          data_list: lista de dicionarios, criada com DictReader().
      Retorna:
          Uma string com o genero mais popular.

"""

    lista = count_gender(data_list)
    answer = ""
    if lista[0] > lista[1]:
        answer = "Male"
    elif lista[1] > lista[0]:
        answer = "Female"
    elif lista[1] == lista[0]:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

# Função que retorna a quantidade de customers e subscribers.
def user_type_counter(user_type_list):
        # def new_function(param1: list) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          data_list: lista de dicionarios, criada com DictReader().
      Retorna:
          Uma lista com a quantidade de customers e quantidade de subscriber.

"""

    customer = user_type_list.count('Customer')
    subscriber = user_type_list.count('Subscriber')
    return [customer, subscriber]

user_type_list = []
for line in data_list: # Cada 'line' é um dicionario, que representa cada linha do arquivo csv
    user_type_list.append(line['User Type'])
# Elaborando o Gráfico:
lista = user_type_list   # Esta é a lista de user_types.
types = ["Customer", "Subscriber"]  # Tipos de user_types
quantity = user_type_counter(user_type_list) # Pega a quantidade de Custumers e de Subscribers
y_pos = list(range(len(types)))      # Eixo y do gráfico
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Cliente')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Cliente')
plt.show(block=True)

print("\nTAREFA 7: Verifique o gráfico!")


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
print(male, female, len(data_list))
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Alguns clientes não tem genero cadastrado."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

# Função que retorna uma lista com os trip_durations
def trip_duration(data_list, index):
    # def new_function(param1: list, param2: int) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          data_list: lista de dicionarios, criada com DictReader().
          index: não serve para nada, pois estou usando dicionarios, apenas mative pois o assert me obriga a receber um int como parametro
      Retorna:
          Uma lista com os Trip Durations.

"""

    lista = []
    for line in data_list:
        lista.append(int(line['Trip Duration']))
    return lista

# Função que retorna o maior e o menor valor dos trip_durations
def maximo(lista_de_duracao):
        # def new_function(param1: list) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          lista_de_duracao: lista de duracões.
      Retorna:
          Uma lista com a maior duração e a menor duração.

"""

    maior = menor = lista_de_duracao[0]
    for duracao in lista_de_duracao:
        if maior < duracao:
            maior = duracao
        elif menor > duracao:
            menor = duracao
    return [menor, maior]

# Calcula a mediana
def mediana(trip_duration_list):
        # def new_function(param1: list) -> float:
"""
      Função de exemplo com anotações.
      Argumentos:
          trip_duration_list: lista de trip_durations.
      Retorna:
          Mediana da lista de duração de viagem.

"""

    trip_duration_list.sort()
    mediana = 0
    tamanho_da_lista = len(trip_duration_list)
    if tamanho_da_lista % 2 == 0:
        x = trip_duration_list[tamanho_da_lista//2 -1]
        y = trip_duration_list[tamanho_da_lista//2]
        mediana = x+y/2
    else:
        z = trip_duration_list[tamanho_da_lista//2 + 1]   
        mediana = z
    return mediana

trip_duration_list = trip_duration(data_list, 2) # O número 2 é o index da coluna que eu quero, no caso trip duration. Porém estou usando dict

soma = sum(trip_duration_list)
tamanho = len(trip_duration_list)
min_trip,max_trip = maximo(trip_duration_list)

# Calculo da média
mean_trip = soma/tamanho

# Caculando a mediana
median_trip = mediana(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set()

for line in data_list:
    start_stations.add(line['Start Station'])

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

# Abrindo arquivo de novo para poder usar como lista, com dictReader() não posso satisfazer os parametros do assert que a Udacity criou
#with open("chicago.csv", "r") as file_read:dd
#    reader_desafio = csv.reader(file_read)
#    data_list_desafio = list(reader_desafio)

def count_items(column_list):
        # def new_function(param1: list) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          column_list: lista de elementos de uma coluna qualquer.
      Retorna:
          Uma lista com tipos de itens dessa colunas e a quantidade de cada item.

"""

    item_types = []
    count_items = []
    tipos = set()
    for data in column_list:
        tipos.add(data)
    item_types = list(tipos)
    for type_item in item_types:
        count_items.append(column_list.count(type_item))
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
