# Q4). Python program to check a String is palindrome or not.


str1 = input("Enter String 1 : ")

lst1 = []
j = 0
while(j < len(str1)):
    lst1.append(str1[j])
    j+=1

 
lst = []

i = len(str1)-1
while(i >= 0):
    lst.append(str1[i])
    i-=1

if(sorted(lst) == sorted(lst1)):
    print("It is a palindrome")


    