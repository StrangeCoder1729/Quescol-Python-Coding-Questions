

str1 = input("Enter String : ")

str1 = list(str1)
str1.sort(reverse = True)

str2 = ''.join(str1)
print(str2)