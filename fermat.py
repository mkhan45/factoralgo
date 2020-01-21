try:
   from factoralgo import gcd, isprime, pollard_util
except:
   from util import gcd, isprime
from util import full_factor, divis
import math

# fermat said that if N = c*d and n is odd,
# N = ((c+d)/2)^2 - ((c - d)/2)^2
# so all this algorithm does is try
# to find c and d based on that.
# It's slower than trial division though.
def fermat(n):
    a = int(math.ceil(n ** 0.5))
    b2 = a * a - n
    b = int(round(b2 ** 0.5))

    if isprime(n): return n

    # doesn't work on 2 or 3 or 5
    for prime in [2, 3, 5]:
        if divis(n, prime):
            return prime

    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = int(round(b2 ** 0.5))

    return a - b


if __name__ == "__main__":
    import sys

    print(full_factor(int(sys.argv[1]), fermat))
