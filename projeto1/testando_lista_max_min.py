lista = [1,2,-1,3,4,40,5,6,7,8,9,10,20,10,11]
maior = menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print(f'Maior:{maior}, Menor:{menor}')

lista.sort()
tamanho_da_lista = len(lista)
print(tamanho_da_lista)
if tamanho_da_lista % 2 == 0:
    print(lista)
    x = lista[tamanho_da_lista//2 -1]
    y = lista[tamanho_da_lista//2]
    print(f'A mediana é {x+y/2}.')
elif tamanho_da_lista % 2 != 0:
    mediana = len(tamanho_da_lista//2 + 1)
    print(mediana)
