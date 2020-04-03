def countdown(x):
    while x > 0:
        yield x
        x -= 1

for i in countdown(50):
    print(i)
