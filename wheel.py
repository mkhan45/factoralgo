try:
   from factoralgo import gcd, isprime
except:
   from util import gcd, isprime
from util import full_factor, divis
import sys


def wheel(n):
    # if n is prime, return n
    if isprime(n): return n

    # this list is gotten by a list of the first few primes and some numbers
    # that are coprime with all those primes
    # i.e. 5 + 2 = 7, 7 + 4 = 11, 11 + 2 = 13, 13 + 4 = 17, 17 + 2 = 19
    # 19 + 4 = 23, 23 + 6 = 29 etc.
    inc = [4, 2, 4, 2, 4, 6, 2, 6]

    # this wheel algorithm doesn't work on primes less than 7, so you have
    # to hardcode them. Anything after 7 just makes it faster.
    for prime in [2, 3, 5, 7, 11]:
        if divis(n, prime):
            return prime

    # if test is true, it means that k is a factor of n
    test = False

    # k is the potential factor and i is the index of the
    # increment list
    k, i = 7, 0
    while not test and k * k <= n:
        test = divis(n, k)
        if test: return k
        k += inc[i]
        i = i + 1 if i < 7 else 0
    return n


if __name__ == "__main__":
    print(full_factor(int(sys.argv[1]), wheel))
