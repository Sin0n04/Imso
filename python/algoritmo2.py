
resul = 1
num = int(input('escribe un numero para saber su factorial: '))


if num < 0:
    print(' el numero introducido es negativo.')
else:
    n = num
    while n > 1:
        resul *= n
        n -= 1

print(' el factorial del numero introducido es ', resul)    