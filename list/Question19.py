# 19). Python Program to print all even numbers in array.

lst = list(map(int,input("Enter numbers : ").split()))

lst2 = [num for num in lst if num%2 ==  0]

print(lst2)