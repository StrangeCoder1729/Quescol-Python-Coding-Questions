# Q13). Python program to insert an element at end of an Array.

lst = []
n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input("Enter number {} : ".format(i+1)))
    lst.append(user_input)

print("List : {}".format(lst))
print("Inputing the number at the end of the array.")
nth = int(input("Enter the Number : "))
lst.append(nth)
print(lst)