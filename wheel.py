from factoralgo import gcd, isprime
from util import factor, divis
import sys

# all functions return a nested tuple like (a, (b, (c, d))) etc
# because it makes recursion easier
def wheel(n):
   # if n is prime, return n
   if isprime(n): return n


   # the increments are basically an optimization because by 
   # doing some math you can tell that all the factors of n will fall on the wheel
   inc = [4, 2, 4, 2, 4, 6, 2, 6]

   # wheel doesn't work on primes less than 7, so you have
   # to hardcode them.
   for prime in [2, 3, 5, 7, 11]:
      if divis(n, prime): return prime, wheel(n // prime)

   # if test is true, it means that k is a factor of n
   test = False

   # k is the potential factor and i is the index of the 
   # increment list
   k, i = 7, 0
   while not test and k * k <= n:
      test = divis(n, k)
      if test: return k, wheel(n // k)
      k += inc[i]
      if i < 7: i += 1 
      else: i = 0
   return n

if __name__ == "__main__":
    print(factor(int(sys.argv[1]), wheel))
