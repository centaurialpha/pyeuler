def largest_palindrome_product():
    max_p = []
    append = max_p.append

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                append(product)

    return max(max_p)


if __name__ == "__main__":
    print(largest_palindrome_product())
