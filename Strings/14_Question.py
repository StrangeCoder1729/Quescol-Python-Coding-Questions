# Q14). Python program to print the highest frequency character in a String.

str1 = input("Enter String : ")

dict = {}
count = 0
for i in str1:
    var = i
    counting = str1.count(i)
    dict.update({var:counting})
    count = 0
 
# print(dict)



key_lst = list(dict.keys())
# print(key_lst)

value_lst = list(dict.values())
# print(value_lst)

maxi = max(value_lst)
value = value_lst.index(maxi)

print(key_lst[value])
 