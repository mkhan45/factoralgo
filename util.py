from collections import Counter

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
