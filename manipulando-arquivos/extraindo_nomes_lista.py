# O programa deve extrair os nomes femininos do arquivo 

lista = []

def nomes(caminho):

    with open(caminho) as f:
        for line in f:
            nome = line.split()[1]
            lista.append(nome)
        return lista

path = 'lista_de_nomes.txt'
print(nomes(path))
print('\n Este texto é impresso quando esse modulo é importado \n')

# Utilizamos o if __name__=='__main__' quando queremos executar testes das funções desse modulo, 
# O que esta dentro desse bloco só será executado quando chamarmos esse script,
# Porém quando impotarmos esse módulo, só será executado o que estiver acima
if __name__=='__main__':
    print('É impresso apenas quando executo o modulo sozinho')
    print(nomes(path))

