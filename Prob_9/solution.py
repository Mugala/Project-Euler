def product():

    for a in range(0,1000):
        for b in range (a,1000):
            for c in range (b,1000):
                if a + b + c == 1000 and c**2 == a**2 + b**2:
                    prod = a * b * c
                    if prod > 0:
                      return (prod)
                  
print(product())