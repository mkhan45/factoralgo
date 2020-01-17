from factoralgo import gcd, isprime, pollard_util
from util import factor, divis
import math

def fermat(n):
   a = int(math.ceil(n**0.5))
   b2 = a * a - n
   b = int(round(b2**0.5))

   if n == 1 or isprime(n):
      return n

   # doesn't work on 2 or 3 
   for prime in [2, 3]:
      if divis(n, prime): return prime, fermat(n // prime)

   # kind
   while (b * b != b2):
      a += 1
      b2 = a * a - n
      b = int(round(b2**0.5))

   return (a - b, fermat(n // (a-b)))

if __name__ == "__main__":
   import sys
   print(factor(int(sys.argv[1]), fermat))
