
i = 1
num = int(input('introduce un numero: '))
while i<= num:
    n = 1
    while n <= num:
        if i >= n:
            print(i, end= ' ')
            n += 1
        else:
            print(' ', end=' ')
            n += 1
    print(end=' \n')
    i += 1
    
        