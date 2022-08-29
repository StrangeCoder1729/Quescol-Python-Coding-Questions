# Q22). Python program to calculate sum of integers in string.

str1 = input("Enter String : ")

lst = []

for i in str1:
    if i.isnumeric() == True:
        lst.append(int(i))

add = 0
for i in lst:
    add += i

print("Sum of the integers in string : {}".format(add))