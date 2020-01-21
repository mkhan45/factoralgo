from collections import Counter

# I wrote gcd and isprime in rust too, but on Windows it will use python since I've only compiled the rust stuff on linux

# trial and error because euler's is too big brain
def gcd(a: int, b: int) -> int:
   if a == 0 or b == 0: return 0
   if a > b: a, b = b, a

   remainder = b % a

   if remainder != 0:
      return gcd(a, remainder)
   else:
      return a

# test i and i + 2 for all the numbers from 5..11..17 etc. to sqrt(n)
# i.e. 5..7..11..13..17..19..23..25 etc.
def isprime(n: int) -> bool:
   return n == 2 or n == 3 or (n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and\
         all(n % i != 0 and n % (i + 2) != 0 for i in range(5, int(n**0.5), 6)))

# turns nested tuple like (a, (b, (c, (c, d)))) into
# a * b * c^2 * d
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
    return "".join(out_str)[:-3]


# turns Tuple(a, b, c, d, ...) into [a, b, c, d, e]
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


# all the factorization functions only return one factor
# so this function recurses through them to find all the
# factors and returns a nested tuple. I could make it return
# a list instead, but initially I made each function recurse
# itself and a tuple was easier than a list
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
