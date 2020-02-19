dic = {}
loop = True
while loop:
    print('Ingrese nombre:')
    name = input('>')
    edad = input('ingrese edad: ')
    dic[name] = edad
    print('quieres repetir? s/n')
    repeat = input()
    if repeat == 'n':
        loop = False

for k, v in dic.items():
    print(' ', dic[k], k)
