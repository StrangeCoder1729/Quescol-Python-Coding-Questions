# Q13). Python program to count Occurrence Of Vowels & Consonants in a String.

str1 = input("Enter the String : ")

str1 = str1.lower()
vowels = ['a','e','i','o','u']

count_1 = 0
count_2 = 0
for i in str1:
    if(i in vowels):
        count_1 += 1
    else:
        count_2 +=1

print(f"Number of Vowels : {count_1}")
print(f"Number of Consonants : {count_2}")