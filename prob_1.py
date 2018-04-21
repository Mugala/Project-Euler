#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
        

#How i did it... 

# def is_factor(n):
#     list_a = []
#     for i in range (1,n):
#         if i % 3 == 0: 
#             list_a.append(i)
#         elif i % 5 == 0:
#             list_a.append(i)

#         x = sum(list_a)
            
#         print(x)

# print(is_factor(1000))  #233168


# A more efficient way to solve the problem
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
print (result)