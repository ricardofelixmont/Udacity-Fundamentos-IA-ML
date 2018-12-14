tupla = (('Nome1', 1, 2), ('Nome2', 3,4),('Nome3', 5,6))

# Podemos iterar cada uma das
for i,j,k in tupla:
    print(f'{i}, {j}, {k}')

# Com zip o resultado é diferente:
for c in zip(*tupla):
    print('{}, {}, {}'.format(*c))
