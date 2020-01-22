# Factoring algorithms

There are four integer factorization algorithms implemented here: trial division, fermat, wheel, and pollard. I implemented all of the integer factorization algorithms in python, but isprime and gcd are written in rust to go faster. As it turns out though, the biggest bottleneck for wheel and pollard is the init time of python itself, however for fermat isprime does matter a lot. I also wrote gcd and isprime in python so that if the rust library isn't compiled everything will still run.

&nbsp;

## `util.py`
All of the factorization algorithms only return one factor of the number given. At first, I wrote each algorithm to be recursive and return a tuple like `(a, (b, (c, c)))` or something similar, but eventually I decided to make a separate function for that, so now each function does just return one factor. In `util.py`, `factor` takes the number and a factorization algorithm to use and outputs the full factor tuple, and then `prettify_factors` turns the tuple into nice looking output. Since it's not really recursive anymore, I could've made `factor` return a list like [a, b, c, d], but it doesn't really impact performance enough to matter so I didn't.

## Trial Division
Trial division is the simplest factorization algorithm; just test every number from 2 to (n // 2 + 1). The code doesn't really need any explanation.

## Fermat
Fermat said that if n = c * d and n is odd, then n = ((c+d)/2)%2 - ((c-d)/2)^2. Essentially all fermat's factorization algorithm is test numbers based on that and solve for the factors. It's even slower than trial division in most cases I've tried.

## Wheel 
Wheel factorization is basically just trial factorization but you only divide by either the first few primes or numbers that are coprime with the first few primes, so hopefully just prime numbers. Wheel runs way faster than either trial division or fermat, and practically the same speed as pollard since they're limited by python init speed for my testing.

## Pollard
Pollard's rho algorithm is the best, fastest algorithm here for big numbers, but it's also the most complicated mathematically. It uses the formula g(x) = (x^2 + 1) mod n to make a pseudorandom sequence that cycles. At the start of the cycle (it does have a start because it's shaped like a rho), the gcd of the difference between the last two numbers and n is either a factor of n, or n. If it is n, then you have to start with the cycle with a different number.
