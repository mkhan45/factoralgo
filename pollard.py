from factoralgo import gcd, isprime
from collections import Counter

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

def unwrap_tup(tup):
   ls = []
   while True:
      if type(tup) == tuple:
         ls.append(tup[0])
         tup = tup[1]
      else:
         ls.append(tup)
         return ls
   return ls

def prettify_factors(tup):
   ls = unwrap_tup(tup)
   cntr = Counter(ls)
   out_str = []
   for base, count in cntr.items():
      if count == 1:
         out_str.append(f"{base} * ")
      else:
         out_str.append(f"{base}^{count} * ")
   return ''.join(out_str)[:-2]

if __name__ == "__main__":
   import sys
   print(prettify_factors(pollard(int(sys.argv[1]))))
