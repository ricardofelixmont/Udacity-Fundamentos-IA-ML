# Criando um iterador:

def iterator(valor):
    i = 0
    while i < valor:
        yield i 
        i += 1
print(iterator(4)) # Ele printa um objeto e não os elementos do iterador.
# Para imprimir os termos do iterador, precisamos iterar sobre ele, por exemplo com for:

for b in iterator(4):
    print(b)
