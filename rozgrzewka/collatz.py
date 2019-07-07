"""
Collatz Algorythm solution
"""

def collatz(x):
    print(x)
    if x == 1:
        return
    elif x % 2 != 0:
        return collatz(x * 3 + 1)
    else:
        return collatz(x // 2)


if __name__ == '__main__':
    number = int(input("Please provide start number"))
    collatz(number)