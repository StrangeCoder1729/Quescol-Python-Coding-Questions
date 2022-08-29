# Q21). Python program to remove repeated character from string.


str1 = input("Enter String : ")


result = ''
for i in str1:

    if i not in result:
        result +=i
     
    
   

print(result)
    

