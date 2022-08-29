# Q23). Python program to print all non repeating character in string.

str1 = input("Enter String : ")

result = ''
counting = 0
for i in str1:
    counting = str1.count(i)
    if counting == 1:
        result += i

print(result)

