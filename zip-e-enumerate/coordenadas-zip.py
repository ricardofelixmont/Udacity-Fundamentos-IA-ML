'''
Use zip para gravar um loop for que cria uma string especificando o rótulo e as coordenadas de cada ponto e acrescenta à lista points. Cada string deve ser formatada como label: x, y, z. Por exemplo, a string para a primeira coordenada deve ser F: 23, 677, 4.
'''

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

'''
lista = zip(labels, x_coord, y_coord, z_coord) # zipando 3 listas

l, x, y, z = list(zip(*lista)) # unziping 3 listas
for a in (x, y, z): # loop para mostrar todas as lista
    print(a)
'''

for lista in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {},{},{}'.format(*lista))
for point in points:
    print(point)

