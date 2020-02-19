act = {}
#fsd
active = True
p = '> '
while active:
    print('enter name: ')
    name = input(p)
    response = input('enter birth date: ')
    act[name] = response
    print('wanna repeat?')
    repeat = input('yes/no')
    if repeat == 'no':
        active = False

for k, v in act.items():
    print('  ', k, v)

