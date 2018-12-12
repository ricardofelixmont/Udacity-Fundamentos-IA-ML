# Fechando arquivos automaticamente: Para nao esquecermos de fechar nenhum arquivo

with open('texto.txt', 'r') as f: # Só consigo usar f dentro da identação, assim que o programa lê uma linha fora desse bloco
                                  # ele fecha o texto.txt automaticamente.
    file_data = f.read() 

print(file_data) # Mesmo com o arquivo fechado ainda podemos usar sua informação, que foi guardada no objeto file_data.


