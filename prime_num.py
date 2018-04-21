print("Enter a number to check if it a prime number...")

n = int(input())

def is_prime(n):
    for i in range (2,n):
        if n % i == 0:
            return False 
        
    return True 

print(is_prime(n))


    