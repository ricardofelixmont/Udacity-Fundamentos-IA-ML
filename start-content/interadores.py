lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

''' Iteradores são iteraveis que nos dao um elemento por vez, não existindo 
100% na memoria. Cada elemento é gerado por vez.'''

def my_enumerate(iterable, start=0): # Argumento padrão = 0
    count = start
    for element in iterable:
        yield element, count
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
