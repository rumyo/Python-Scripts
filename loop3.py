loop = True


while loop:
    try:
       age = int(input('ingrese edad \n'))
    except ValueError:
        print('Error, ingrese un numero valido')
        continue
    if age > 18:
        print('eres mayor')
    else:
        print('Eres menor')

    r = input('Quiere volver a intentar? s/n \n')
    if r == 'n':
        print('Usted ha cerrado el programa')
        loop = False
