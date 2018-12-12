'''filter() é uma função interna de ordem superior que aceita uma função e um iterável como entradas e devolve um iterador com os elementos do iterável para os quais a função retorna o valor true. O código abaixo usa filter() para obter os nomes em cities que possuem menos de 10 caracteres de tamanho para criar a lista short_cities. Execute um teste para ver o que acontece.

Reescreva esse código para ser mais conciso, substituindo a função is_short por uma expressão lambda definida dentro da chamada de filter().'''


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

'''
short_cities = list(filter(is_short, cities))
print(short_cities)
'''
short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)
