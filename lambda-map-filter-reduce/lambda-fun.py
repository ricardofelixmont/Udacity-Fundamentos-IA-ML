from math import sin, cos



if __name__=='__main__':

    # Map(func, iteravel) aplica a funcao a todos os itens do iteravel.
    iteravel = [0, 30, 45, 60, 90]
    print(list(map(lambda x: sin(x), iteravel)))

    # Não funciona se eu jogar o sen(x) direto: map(sin(x), iteravel)
    # pois ele nao reconhece o iteravel como argumento, para isso preciso de
    # uma função lambda
    
    iteravel2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Podemos chamar dois iteravel da seguinte forma:
    x = list(map(lambda x,y: cos(x)+sin(y), iteravel2, iteravel))
    print(x)
    
    # As expressões lambda acima estão sendo usadas como funcões anonimas
