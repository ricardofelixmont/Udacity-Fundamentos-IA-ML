scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
print(scores)
print(scores.items())
lista = [chave for chave, valor in scores.items() if valor > 65]
print(lista)
