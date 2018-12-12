# Gerador de expressõeos

from math import pi, sin

# Gera um iteravel do tipo dicionario
# onde x é a chave e seno do angulo em rad é o valor
# O resultado é um dicionario com o angulo como chave e o seno como valor
sine_dictionary = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_dictionary)



# Para gerar uma lista/iteravel de quadrados por exemplo:
lista_de_quadrados = [x**2 for x in range(0,10)]
print(lista_de_quadrados)


# Para gerar um iterador de quadrados por exemplo:
iterador_de_quadrados = (x**2 for x in range(0,10))
print(iterador_de_quadrados) # Printa o objeto iterador de quadrados

# O item abaixo mostra os itens do iterador de quadrado(é preciso iterar para objeto os itens de um 
# iterador
for item in iterador_de_quadrados:
    print(item)

