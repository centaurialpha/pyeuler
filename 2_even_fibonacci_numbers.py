def even_fibo_numbers(n=4000000):
    npar = []
    append = npar.append
    a, b = 0, 1
    while b < n:
        fib = a + b
        if fib % 2 == 0:
            append(fib)
        a, b = b, fib
    return sum(npar)

if __name__ == "__main__":
    print(even_fibo_numbers())
