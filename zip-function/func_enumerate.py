# Cada nome da lista nomes precisa ter o peso da lista pesos 'Barney Stinson 72'

nomes = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
pesos = [72, 68, 72, 66, 76]
lista = []

for i, nome in enumerate(nomes):
    nome += ' ' +  str(pesos[i])
    lista.append(nome)

print(lista)


# MELHOR FORMA DE FAZER:
for i, nome in enumerate(nomes):
    nomes[i] = nome + ' ' + str(pesos[i])
print(nomes)
