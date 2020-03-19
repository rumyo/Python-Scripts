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
    while r is not 'n' and r is not 's':
        print('Introduzca "s" si desea volver a intentar o "n" si desea cerrar el programa')
        r = input()
    if r == 'n':
        print('Usted ha cerrado el programa')
        loop = False

