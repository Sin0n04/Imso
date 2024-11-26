ult = 1
penult = 1
tope = int(input('escribe un numero tope: '))

print('1')
print('1')

while penult + ult <= tope:
    siguiente = penult + ult
    penult = ult
    ult = siguiente
    print(siguiente)
    