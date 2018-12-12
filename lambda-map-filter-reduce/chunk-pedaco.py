# Both call of range below has the same output
#print(list(range(25)))
#print(list(range(0,25)))


# Criar uma função que mostra pedaços do iteravel abaixo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]       
def chunker(lista, size):
    ''' O range gera um numero de size em size. E a cada numero que ele gera, é returnado com yield
        uma sublista : lista[i: i+ size]'''
    for i in range(0, len(lista), size):
        yield lista[i: i+ size]

print(list(chunker(lista, 4))) # Imprime uma lista de listas, uma de cada vez, diminuindo o uso da memeoria.
