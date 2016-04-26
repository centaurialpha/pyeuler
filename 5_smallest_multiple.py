"""
It takes a long time but does the job
"""


def smallest_multiple():
    n = 1
    b = False
    while True:
        index = 1
        while index <= 20:

            if n % index == 0:
                b = True
            else:
                b = False
                index = 21
                continue
            index += 1
        if b:
            print(n)
            break
        n += 1


if __name__ == "__main__":
    smallest_multiple()
