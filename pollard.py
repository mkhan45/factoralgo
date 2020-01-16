from factoralgo import gcd, isprime

# def gcd(a, b):
#    if a > b:
#       a, b = b, a

#    # fac = b // a
#    remainder = b % a

#    if remainder != 0:
#       return gcd(a, remainder)
#    else:
#       return a

# def isprime(n: int):
#    return n % 2 != 0 and all(n % i != 0 for i in filter(lambda i: isprime(i), range(3, int(n**0.5) + 1, 2)))

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

import sys
print(pollard(int(sys.argv[1])))
