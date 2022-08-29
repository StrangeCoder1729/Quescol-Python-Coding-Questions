# 16). Python Program to delete given element from Array.

lst = list(map(int,input("Enter numbers : ").split()))

delete = int(input("Which number you want to delete : "))

lst.remove(delete)
print(lst)