def palabra():
    word = ''
    for w in 'universidad':
         word += w
         yield word

lista = list(palabra())
print(lista)
