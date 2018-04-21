start_point =1
input_number = 10

def range_generator(input):

    range_list=list(range(1,input+1))
    return range_list

def increment_start():
    global start_point

    start_point+=1

def is_divisible(number1,number2):
    if number1 % number2 == 0:
        return True
    else:
        return False

range_list = range_generator(input_number)
index_counter = 0

while index_counter < len(range_list):

    print(index_counter)
    
    if is_divisible(start_point,range_list[index_counter]):
         index_counter +=1
         continue
    else:
        index_counter = 0
        increment_start()

print(start_point)




# n = 0
# def num(n):
#     list_a = range(1,11)
#     for i in list_a:
#             print(i) 
    
# print(num(n))   

# def div_num
         

