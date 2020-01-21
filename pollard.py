try:
   from factoralgo import gcd, isprime
except:
   from util import gcd, isprime
from util import full_factor

def pollard(n):
    if isprime(n): return n

    # unlike the others, the only prime pollard
    # doesn't work for is 2 so it doesn't make sense
    # to have a whole list
    if n % 2 == 0: return 2

    # pollard doesn't work on perfect squares
    if int(n ** 0.5) == n ** 0.5:
        return int(n ** 0.5)

    # x**2 - 1 also works but I like being positive
    def g(x, n):
        return (x ** 2 + 1) % n

    # cycle finding
    x, y, d = 2, 2, 1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x - y), n)

    return d


if __name__ == "__main__":
    import sys
    print(full_factor(int(sys.argv[1]), pollard))
