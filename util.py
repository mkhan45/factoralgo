from collections import Counter

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

def factor(n, factorfn):
   return prettify_factors(factorfn(n))
