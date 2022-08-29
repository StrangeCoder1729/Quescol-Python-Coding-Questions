# Q16). Python program to count alphabets, digits and special characters.

str1 = input("Enter String : ")

count_alpha = 0
count_numeric = 0
count_special = 0
for i in range(0,len(str1)):
    if(str1[i].isalpha() == True):
        count_alpha +=1
    elif(str1[i].isnumeric() == True):
        count_numeric +=1
    else:
        count_special +=1

print("ALphabets in string: {}".format(count_alpha))
print("Numerics in string: {}".format(count_numeric))
print("Special in string: {}".format(count_special))
