# Try except uses:

#number = int(input('Type a number: '))
#print(f'{number}')
# O codigo acima vai dar ValueError se nao digitarmos um número inteiro


# Podemos resolver esse problemas usando o Try statement
'''
try:
    number2 = int(input('Type a number: '))
except: # Qualquer exceção que o programa der, vai cair nessa condição
    print('Você digitou um valor invalido ou uma string.')
    
print(f'fora do try') # Sempre executado depois do try  ou except
'''

'''
# Caso eu queira que o 'fora do try' seja executado sempre após o try:
try:
    number3 = int(input('Type a number: '))
except:
    print('Você digitou um valor invalido ou uma string.')
finally:
    print(f'{number3}') # Se eu digitar uma string, ele entra no except e quando for printar o finally ele vai dar erro
                        # pois nao vai existir uma variavel 'number3' para printar.
'''
'''
# Posso especificar a excessão que quero tratar:
try:
    number4 = int(input('Type a number: '))
except ValueError: # Dessa forma posso tratar todos as exceções individualmente
    print('ValueError: Please try again!')
except (NameError, KeyboardInterrupt): # Podemos criar uma tupla de exeções tratadas por esse bloco de excessão
    print('Name Erros, tente novamente!')
finally:
    print('Saindo do Try')
'''

# Usando else caso o try seja executado:
try:
    number5 = int(input('Type a number: '))
except:
    print('Exception found')
else:
    # Se o python nao encontrar excessões durante a execucao do try, ele executa o codigo que esta dentro do bloco else:
    print('else é executado logo apos o try')
finally:
    # Mesmo que houver um except ele executará o codigo dentro do finally antes da interrupçao do programa
    print('finally é executado logo apos o try ou o except')
