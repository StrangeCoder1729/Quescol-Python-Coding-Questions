# Q6). Write a program in Python to find second highest number in an integer array.

lst = []
n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input(f"Enter number {i+1} : "))
    lst.append(user_input)

lst.sort(reverse = True)
print("The Second Maximum number in the array is {}".format(lst[1]))