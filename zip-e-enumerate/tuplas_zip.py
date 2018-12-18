cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

name = () # não da erro mas nao é necessario colocar
heights = () # o mesmo da linha de cima

names, heights = zip((*cast)) #nesse caso para deszipar é necessario usar o zip()
print(names, heights)

for tupla in cast:
    print('{}: {}'.format(*tupla))   # dentro do .format() posso usar o zip normalmente.
