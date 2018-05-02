
#Function to test and see if a number is a prime )_
def is_prime(n):
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False 
        
    return True 

#Function to create a list and loop to test if number is prime

def test():
    list_prime = []
    for x in range(2,2000000):
        if is_prime(x) == True:
            list_prime.append(x)
    p = sum(list_prime)

    print(p)


print(test())




