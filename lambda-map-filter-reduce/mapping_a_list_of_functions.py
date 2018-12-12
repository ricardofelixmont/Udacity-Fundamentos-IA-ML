from math import sin, cos, tan, pi

# aplicar varias funções a um objeto, no caso, o número pi

def map_fun(number, functions):
    res = []
    for func in functions:
        res.append(func(number))
    return res

if __name__=='__main__':

    lista = (sin, cos, tan)

    print(map_fun(pi, lista)) # Retorna uma lista

    # Fazendo com uma lista de compreensão:
    print([func(pi) for func in lista]) # Vemos que simplifica muito(também retorna uma lista)
