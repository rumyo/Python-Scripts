def count(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

lista = list(count(100))
print(lista)

for i in count(100):
    print(i)
