def create_groups(items, n):
    """Splits items into n groups of equal size, although the last one may be shorter."""
    # determine the size each group should be
    
    # Aqui pode ocorrer uma excessão de divisao por zero
    try: 
        size = len(items) // n  # this line could cause a ZeroDivisionError exception
    except ZeroDivisionError:
        print('WARNING: Returning empty list. Please use a nonzero number.')
        return [] #Se não colocar o return [](retorna uma lista vazia) vai dar erro de
                  #TypeError: 'NoneType' object is not iterable, pois é necessario pelo menos uma lista vazia para iterar.
                    
    else:
        # create each group and append to a new list
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        # print the number of groups and return groups    
        print("{} groups returned.".format(n))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

# Essa ultima linha é só pra testar a divisão por zero. Precisa receber pelo menos uma lista vazia como retorno da
# função create_groups(), do contrario da um erro de TypeError: 'NoneType' object is not iterable, que acontece
# Quando a função nao retorna nada, entao a variavel 'group' seria um objeto do tipo None.
print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
