# matriz transposta
matriz = ((0,1,2),(3,4,5),(6,7,8),(9,10,11))

# O processo de unzip ja faz uma transposição de matrizes.
# Podemos guardar a matriz em um novo iterável:
print('-='*10)
x = tuple(zip(*matriz))
print(x)

# Ou podemos criar um iterador para a matriz, o que economiza memoria.
print('-='*10)
for linha in zip(*matriz):
    print(linha)
