# Q12). Python program to delete vowels in a given string.

string = input("Enter the String : ")

string = string.lower()
vowels = ['a','e','i','o','u']

result = ''
for i in string:
    if i in vowels:
        i = ''
    result += i

print(result)

        
