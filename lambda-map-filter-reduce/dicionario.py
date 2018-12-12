dicionario = {'Ricardo':25, 'Renata': 24, 'Érika':24, 'Rafael':23, 'Eliane':40}

print(dicionario.items()) # items() retorna uma lista de tuplas com chave valor

lista_de_compreensao = [chave for chave,valor in dicionario.items() if valor < 40]
print(lista_de_compreensao)

# Posso usar uma lista de compreensão dentro da expressão lambda:
x = lambda dicionario: [chave for chave, valor in dicionario.items() if valor < 40]
print(x(dicionario)) # Passando um dicionario como argumento

