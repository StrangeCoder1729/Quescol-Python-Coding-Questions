# Q11). Python program to reverse an Array in two ways.


lst = []
n = int(input("Enter n : "))

for i in range(0,n):
    user_input = int(input(f"Enter Number {i+1} : "))
    lst.append(user_input)

lst.reverse()
print(lst)