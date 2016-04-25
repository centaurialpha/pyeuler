def largest_prime_factor(n=600851475143):
    factors = []
    append = factors.append
    d = 2
    while n > 1:
        while n % d == 0:
            append(d)
            n /= d
        d += 1
    return max(factors)

if __name__ == "__main__":
    print(largest_prime_factor())
