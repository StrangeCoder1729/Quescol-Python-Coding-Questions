#Q22). Python Program to find Smallest number among three.

def smallest(lst):
    return min(lst)


n = int(input("Enter n : "))
lst = []
for i in range(0,n):
    user_input = int(input(f"Enter number {i+1} : "))
    lst.append(user_input)

print(smallest(lst))