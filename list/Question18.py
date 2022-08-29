# 18). Python Program to find sum of array elements.

 

lst = list(map(int,input("Enter numbers : ").split()))

add = 0
for num in lst:
    add += num

print("Sum of all the numbers in the list is {}".format(add))