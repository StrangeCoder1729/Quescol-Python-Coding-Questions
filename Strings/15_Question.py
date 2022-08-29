# Q15). Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.


vowels = ['a','e','i','o','u']

str1 = input("Enter String : ")
str1 = str1.lower()
for i in range(0,len(str1)):
    if str1[i] in vowels:
        str1 = str1.replace(str1[i],'-')
        break

print(str1)