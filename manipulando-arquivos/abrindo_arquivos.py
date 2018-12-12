f = open('texto.txt', 'r')
print(f) # Aqui vemos que f é um objeto de texto do python.

file_data = f.read() # Lê o arquivo completo
print(file_data)
f.close()            # Sempre que terminamos de utilizar um arquivo em python, precisamos fecha-lo
                     # para economizar recursos da máquina, pois cada arquivo usa um identificador de arquivos python

