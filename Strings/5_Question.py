# Q5). Python program to check given character is vowel or consonant.


str1 = input("Enter string : ")
str1 = str1.lower()
if('a' in str1 or 'e' in str1 or 'i' in str1 or 'o' in str1 or 'u' in str1):
    print('Its a vowel')
else:
    print("its a consonant")