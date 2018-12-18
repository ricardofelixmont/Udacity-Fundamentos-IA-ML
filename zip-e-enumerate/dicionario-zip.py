cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

dicionario = dict(zip(cast_names, cast_heights))
print(dicionario)

for chave, valor in dicionario.items():
    print(f'{chave}:{valor}')
