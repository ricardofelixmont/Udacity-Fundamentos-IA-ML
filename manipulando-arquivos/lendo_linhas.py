# O método readline() le uma linha por vez, a primeira chamada le a 1° linha
# a segunda chamada le a 2° linha e assim por diante.
with open('texto.txt', 'r') as f:
    linha1 = f.readline()
    linha2 = f.readline()
    linha3 = f.readline()

print(linha1)
print(linha2)
print(linha3)
