import csv
with open('cepbr_endereco.csv', 'r', encoding='latin-1') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)
