# Q8). Write a program in Python to remove duplicate elements form array.

lst = []
n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input("Enter number {} : ".format(i+1)))
    lst.append(user_input)

print("Original Array : {}".format(lst))
couting = 0
lst2 = []
for num in lst:
    
    if num not in lst2:
        lst2.append(num)
        
print("Array which does not have duplicates : {}".format(lst2))