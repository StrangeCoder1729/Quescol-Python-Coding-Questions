# Q1). Write a program in Python for, In list 1-100 numbers are stored, one number is missing how do you find it.

lst = []
n = int(input("Enter n : "))

for i in range(1,n):
    user_input = int(input(f"Enter input {i} : "))
    lst.append(user_input)

sum1 = (n*(n+1))/2
# print(f"Sum = {sum1}")
add = 0
for num in lst:
    sum1 = sum1 - num
    
print(f"Missing number is {sum1}")






