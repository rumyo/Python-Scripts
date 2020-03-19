print('Bienvenido a calculadora simple')
print('Introduzca el tipo de operacion que desea realizar:')
op = input('sum, res, div, mult \n')

print('Introduzca el valor 1')
a = float(input())
print('Introduzca el valor 2')
b = float(input())

if op == 'sum':
 c = a + b
elif op == 'res':
 c = a - b
elif op == 'div':
 c = a / b
else:
 c = a * b

print(c)
