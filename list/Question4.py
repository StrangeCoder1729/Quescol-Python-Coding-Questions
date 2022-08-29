# Q4). Write a program in Python for, How to compare two array is equal in size or not.

lst1 = []
lst2 = []

n1 = int(input("Enter range for list 1 : "))
n2 = int(input("Enter range for list 2 : "))
print()
print("For the List 1 :- ")
for i in range(0,n1):
    user_input1 = int(input(f"Enter number {i+1} : "))
    lst1.append(user_input1)

print()
print("For the List 2 :- ")
for i in range(0,n2):
    user_input = int(input(f"Enter Number {i+1} : "))
    lst2.append(user_input)

if (len(lst1) == len(lst2)):
    print("The Two arrays are equal in size")
else:
    print("The Two arrays are not in equal in size")
