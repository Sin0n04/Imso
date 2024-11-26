import random
acierto = False
i = 1
num= random.randint(1,1000)

while i <= 10 and acierto == False:
    n = int(input('escribe un numero entre 1 y 1000: '))
    if n > num:
        print(' te has pasado ')
    elif n < num:
        print('te has quedado corto ')
    elif n == num:
        acierto = True
        print(' has acertado en ', i, ' intentos')
    i += 1


if i > 10:
        print('te has quedado sin intentos:')
        print(' el numero es: ', num)