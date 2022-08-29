# 15). Python Program to delete element at end of Array.

lst =list(map(int,input("Enter Numbers : ").split()))

lst.remove(lst[len(lst)-1])

print(lst)