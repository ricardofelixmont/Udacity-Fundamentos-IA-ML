# A funcção map() é interna do python e de ordem superior(aceita outras funções como argumento.
# map(função, lista) -> a função map aplica a função a cada elemento da lista

numbers = [

              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

'''def mean(num_list):
    
    return sum(num_list) / len(num_list)
'''
# A expressão lambda a seguir é uma função anônima
averages = list(map(lambda numbers: sum(numbers) / len(numbers), numbers))
print(averages)
