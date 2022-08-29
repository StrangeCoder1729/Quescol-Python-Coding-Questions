#Q8). Write a program in Python to find greatest among three integers.

def greatest(lst):
    return max(lst)


lst = []
for i in range(0,3):
    user_input = int(input(f"Enter number {i+1}: "))
    lst.append(user_input)

res = greatest(lst)
print(f"Maximum number is {res}")