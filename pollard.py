from factoralgo import gcd, isprime, pollard_util
from util import factor

def pollard(n):
   if isprime(n):
      return (n)
   if n % 2 == 0:
      return 2, pollard(n // 2)

   x = 2
   y = 2
   d = 1

   def g(x, n):
      return (x**2 + 1) % n

   while d == 1:
      x = g(x, n)
      y = g(g(y, n), n)
      d = gcd(abs(x - y), n)
      if d == 0:
         return (int(n**0.5), int(n**0.5))

   if d == n:
      return None
   else:
      f1 = d
      f2 = n // f1
      if isprime(f2):
         return (f1, f2)
      else:
         return (f1, pollard(f2))

if __name__ == "__main__":
   import sys
   print(factor(int(sys.argv[1]), pollard))
