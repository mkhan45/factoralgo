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

## Benchmarks

Python startup time is around 12.7 ms:
```
hyperfine --warmup 5 'python -c ""'
Benchmark #1: python -c ""
  Time (mean ± σ):      12.7 ms ±   0.4 ms    [User: 10.4 ms, System: 2.5 ms]
  Range (min … max):    12.1 ms …  14.0 ms    215 runs
```

```
hyperfine --warmup 5 "python trial_division.py $num" "python fermat.py $num" "python wheel.py $num" "python pollard.py $num"
Benchmark #1: python trial_division.py 59234567
  Time (mean ± σ):     627.6 ms ±   3.7 ms    [User: 625.0 ms, System: 1.5 ms]
  Range (min … max):   621.3 ms … 632.6 ms    10 runs

Benchmark #2: python fermat.py 59234567
  Time (mean ± σ):      1.952 s ±  0.022 s    [User: 1.946 s, System: 0.002 s]
  Range (min … max):    1.925 s …  1.980 s    10 runs

Benchmark #3: python wheel.py 59234567
  Time (mean ± σ):      14.7 ms ±   0.4 ms    [User: 12.7 ms, System: 2.0 ms]
  Range (min … max):    14.0 ms …  15.9 ms    185 runs

Benchmark #4: python pollard.py 59234567
  Time (mean ± σ):      14.9 ms ±   0.6 ms    [User: 12.8 ms, System: 2.1 ms]
  Range (min … max):    14.0 ms …  18.3 ms    176 runs

Summary
  'python wheel.py 59234567' ran
    1.01 ± 0.05 times faster than 'python pollard.py 59234567'
   42.69 ± 1.20 times faster than 'python trial_division.py 59234567'
  132.82 ± 3.93 times faster than 'python fermat.py 59234567'
```

For bigger numbers I took out fermat and trial division cause they're slow
```
hyperfine --warmup 5  "python wheel.py $num" "python pollard.py $num"
Benchmark #1: python wheel.py 592345678901234567
  Time (mean ± σ):      5.203 s ±  0.005 s    [User: 5.190 s, System: 0.002 s]
  Range (min … max):    5.197 s …  5.210 s    10 runs

Benchmark #2: python pollard.py 592345678901234567
  Time (mean ± σ):      5.208 s ±  0.004 s    [User: 5.194 s, System: 0.003 s]
  Range (min … max):    5.203 s …  5.216 s    10 runs

Summary
  'python wheel.py 592345678901234567' ran
    1.00 ± 0.00 times faster than 'python pollard.py 592345678901234567'
```

It seems like they're pretty much exactly the same speed, and wheel factorization can easily be made faster by using a larger basis. Also, pollard's can very rarely be wrong when gcd(|a - b|, n) is just n. I also didn't really try to optimize the code but I doubt that makes a difference.
