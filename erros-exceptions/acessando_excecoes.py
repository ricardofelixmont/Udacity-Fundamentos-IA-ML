# Podemos acessar as exceções mesmo quando as estamos tratando:

# Aqui se digitarmos algo diferente de um inteiro ele mostra a exceções ValueError.
'''
try:
    number = int(input('type a number: '))
except ValueError: # Porém dessa forma nao podemos ver a descrição da exceção completa.
    print('Exception ValueError')
'''

# Outra forma de fazer, mostrando as excessões:
'''
try:
    number = int(input('Type a number: '))
except ValueError as e:
    print(f'Ocorreu um ValueError: {e}')
finally:
    print('Saindo do try')
'''

# No exemplo acima abrimos a excessão especifica, mas podemos usar de forma geral.
try:
    number = int(input('Type a number: '))
except Exception as e: # Exception é a classe base para todas as exeções internas.
    print('Exessão: {}'.format(e))
else:
    print(f'{number}')
finally:
    print('Saindo do try.')
