def area(lado_a, lado_b = 10):
    area = lado_a * lado_b
    print(lado_a, lado_b)
    return area

print(area(2, 3)) # Passagem de argumento por posição
print(area(lado_b = 3, lado_a = 2))  # Passagem de argumento por nome(posso inverter as posições mas tenho que escrever o nome das variaveis de argumento)
print(area(2)) # quando omitimos uma das variaveis de argumento, ele coloca o valor padrao

