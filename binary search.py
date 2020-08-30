import random

def binary_search(list,lower_limit,upper_limit,number):

    if upper_limit >= lower_limit:
        half= (lower_limit + upper_limit ) // 2
        if number == list[half]:
            return half
        elif number < list[half]:
            return binary_search(list,lower_limit,half-1,number)  
        else:
            return binary_search(list,half+1,upper_limit,number)  
    else:
        return -1
random_number_list=[]
x=0
while x<50:

    random_number_list.append(random.randint(1,100))
    x += 1

length_of_list = len(random_number_list)
sorted_list = random_number_list.sort()

print(random_number_list)
number_to_find = int(input("Enter number between 1 to 100"))

start = 0
print(binary_search(random_number_list , start ,  length_of_list-1 , number_to_find))




