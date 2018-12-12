names = input('digite os nomes: ').split().title()
assignments = input('Digite os assignments: ').split()
grades = input('Digite as notas: ').split()


message = 'Hi {},This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.'

for nome, tarefa, nota in names, assignments, grades:
    notaPotencial = nota + 2*assignments
    print(message.format(nome, tarefa, nota, notaPotencial))
