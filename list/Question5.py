# Q5). Write a program in Python to find largest and smallest number in array.


lst = []
n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input(f"Enter Number {i+1} : "))
    lst.append(user_input)


print("Maximum number in the list is {}".format(max(lst)))
print("Minimum number in the list is {}".format(min(lst)))