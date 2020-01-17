from factoralgo import gcd, isprime
from util import factor
import sys

def wheel(n):
   if isprime(n):
      return n

   test = False
   inc = [4, 2, 4, 2, 4, 6, 2, 6, 4]
   for prime in [2, 3, 5, 7, 11]:
      if divis(n, prime): return prime, wheel(n // prime)
   k, i = 7, 1
   while not test and k * k <= n:
      test = divis(n, k)
      if test: return k
      k += inc[i]
      if i < 8: i += 1 
      else: i = 0
   return n

def divis(n, k):
   return n % k == 0

if __name__ == "__main__":
    print(factor(int(sys.argv[1]), wheel))
