# function to change the product into a string reverse 
def is_palindrome(n):
    return str(n) == str(n)[::-1]


def palindrome_product():
    pal = 0

    for i in range(100,1000):
        for n in range (i,1000):
            p = i * n
            if is_palindrome(p) and p > pal:
                pal = p

    return pal

print(palindrome_product())