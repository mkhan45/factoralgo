from util import divis, full_factor

def repeated_factor(n):
   for i in range(2, n // 2 + 1):
      if divis(n, i):
         return i

   return n

if __name__ == "__main__":
    import sys
    print(full_factor(int(sys.argv[1]), repeated_factor))
