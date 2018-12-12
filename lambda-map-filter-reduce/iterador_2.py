# Crie os seguintes objetos com geradores de expressões: dicionario(iteravel), lista(iteravel), iterador

iteravel_dicionario = {x: x**2 for x in range(10)}
print(iteravel_dicionario)         # mostra o dicionario
print(iteravel_dicionario.items()) # Criar uma lista de tuplas com chave:valor
print(iteravel_dicionario[4])      # Como é um iteravel, posso acessar seus valores com as chaves.

iteravel_lista = [c**2 for c in range(10)]
print(iteravel_lista) # Cria um iteravel tipo do tipo lista com o quadrados dos elementos do iterador range
print(iteravel_lista[4]) # como é um iteravel, ele esta sempre na memoria. Entao posso acessar seus valores pelo indice

iterador = (c**2 for c in range(10)) # Os parentesis diferenciam o gerador de iterador de um gerador de iteravel
print(iterador) # Não consigo print o iterador dessa forma, eu preciso iterar sobre seus elementos.

'''for c in iterador:  
    print(c, end=' ')
print('\n')
'''
for c in iterador:  # posso colocar o filtro que eu quiser nesse iterador
                    # Não posso fazer duas chamadas para o mesmo iterador?
    if c < 20:
        print(c, end=' ')
print('\n')

