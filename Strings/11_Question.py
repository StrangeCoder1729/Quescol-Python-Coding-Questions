# Q11). Python program to convert lowercase vowel to uppercase in string.


str1 = input("Enter the String : ")


lst = list(str1)
vowels = ['a','e','i','o','u']
 
# print(lst)
# for i in range(0,len(str1)):
#     if str1[i] in vowels:
#         inde = lst.index(str1[i])
#         print(inde)
#         capital = str1[inde].upper()
#         print(capital)
#         str1 = capital + str1[inde::]
#     inde = 0

result ='' 
for i in str1:
    if i in vowels:
        inde = lst.index(i)
        # print(inde)
        capital = str1[inde].upper()
        # print(capital)
        i = str1[inde].replace(i,capital)
    result += i

print(result)
# print(str1)