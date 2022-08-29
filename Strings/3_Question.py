# Q3). Python Program to check if two Strings are Anagram.

str1 = input("Enter String 1 : ")
str2 = input("Enter String 2 : ")
 

sort1 = sorted(str1)
sort2 = sorted(str2)
lst_str1 = []
for i in sort1:
    if(i == ' '):
        continue
    lst_str1.append(i)

lst_str2 = []
for j in sort2:
    if(j ==' '):
        continue
    lst_str2.append(j)
 
print(lst_str1)
print(lst_str2)
if(lst_str1 == lst_str2):
    print("Its an Anagram !!")