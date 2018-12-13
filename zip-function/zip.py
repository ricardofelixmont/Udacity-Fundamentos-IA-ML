# ZIP FUNCTION
# zip é um iterador built-in Python. Passamos iteraveis e ele os une em uma estrutura só
nomes = ['Lucas', 'Ewerton', 'Rafael']
idades = [25, 30, 24]

nomes_idades = zip(nomes, idades)
print(nomes_idades) # Mostra o objeto do tipo zip()
#como zip() é um iterador, precisamos iterar sobre ele para mostrar seus elementos
for nome in nomes: # Dessa forma ele nao fica guardado na memoria como uma variavel separada
    print(nome)

# Tambem podemos atribuir esse zip a uma lista:
nomes_idades = list(zip(nomes, idades))
print(nomes_idades)
