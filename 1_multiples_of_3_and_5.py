

def multiples_of_3_and_5():
    multiples = (n for n in range(1000)
                 if n % 3 == 0 or n % 5 == 0)
    return sum(multiples)

print(multiples_of_3_and_5())
