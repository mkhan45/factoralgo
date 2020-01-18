from collections import Counter

def prettify_factors(tup):
   ls = sorted(unwrap_tup(tup))
   cntr = Counter(ls)
   out_str = []
   for base, count in cntr.items():
      # turns tuple base(count) into string base^count
      # and adds it to the list
      if base != 1:
         if count == 1:
            out_str.append(f"{base} * ")
         else:
            out_str.append(f"{base}^{count} * ")
   return ''.join(out_str)[:-3]

def unwrap_tup(tup):
   # turns Tuple(a, b, c, d, ...) into [a, b, c, d, e]
   ls = []
   while True:
      if type(tup) == tuple:
         ls.append(tup[0])
         tup = tup[1]
      else:
         ls.append(tup)
         return ls
   return ls

def factor(n, factorfn):
   fac = factorfn(n)
   if n == 1 or fac == 0 or n // fac == 0:
      return n
   return (fac, factor(n // fac, factorfn))

def full_factor(n, factorfn):
   return prettify_factors(factor(n, factorfn))

# tests if n is divisible by k
def divis(n, k):
   return n % k == 0
