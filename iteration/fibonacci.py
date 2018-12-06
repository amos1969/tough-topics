def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

itr = fib()
for _ in range(100):
    print(next(itr))