'''
Find gcd of two given number using Euclid's algorithms
'''


def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a


if __name__ == '__main__':
    print(gcd(60, 96))
    print(gcd(20, 8))
