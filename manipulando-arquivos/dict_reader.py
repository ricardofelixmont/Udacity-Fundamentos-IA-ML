# Abrindo arquivos csv, como OderedDict, dicionario ordenada. 
import csv


with open('relatorio.txt', mode='r') as csv_file:
    # Por padrão, o dictReader pega os itens da primeira linha como chave
    # O arquivo está guardado em csv_reader
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        # Podemos acessar os valores de cada linha da seguinte forma: row['chave']
        print('{}, {}, {}, {}, {}'.format(row['moeda'], row['valor'], row['mudanca'], row['porcentagem'], row['data']))

        
