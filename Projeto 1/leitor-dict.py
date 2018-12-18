import csv

with open('chicago.csv', 'r') as csv_file:
    arquivo = csv.DictReader(csv_file)
    lista_dict = list(arquivo) # Guardando o arquivo .txt 
    count = 0 
    for linha in lista_dict:
        if count == 0:
            print(linha['Start Time'])
            count += 1
