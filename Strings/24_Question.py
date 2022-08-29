# Q24). Python program to copy one string to another string.

str1 = input("Enter String 1 : ")

str1 = list(str1)
# print(str1)

str2 = []

for i in range(0,len(str1)):
    str2.append(str1[i])

str3 = ''.join(str2)
print(str3)