# Q18). Python program to remove blank space from string.

str1 = input("Enter String : ")

result = ''
for i in range(0,len(str1)):
    if(str1[i] == ' '):
        continue
    result += str1[i] 

print(result)