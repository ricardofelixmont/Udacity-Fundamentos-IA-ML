# Quando o script que quero acessar esta no mesmo diretorio do script para o qual eu quero importar:
# Nesse caso o script é chamado de modulo, um módulo é um arquivo com definições e instruções do Python
# Quando importamos um módulo como esse, o python cria um objeto(com o nome do módulo) chamado 'extraindo_nomes_lista'
import extraindo_nomes_lista #ele importa o arquivo e executa tudo que ouver nele.
print('\n')

# Para facilitar na hora de digitar o nome do modulo podemos usar a seguinte sintaxe:
# Abaixo eu posso usar qualquer variavel ou função/metodo daquele script
print(extraindo_nomes_lista.nomes('lista_de_nomes.txt'))
print('\n')

# Para facilitar na hora de digitar o nome do modulo podemos usar a seguinte sintaxe:
import extraindo_nomes_lista as enl
print(enl.nomes('lista_de_nomes.txt'))
