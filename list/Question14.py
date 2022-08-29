# 14). Python program to insert element at a given location in Array.


lst = list(map(int,input("Enter elements : ").split()))

print("Inputing the element :-") 
print()
temp = 0 
user_input = int(input("Enter Number : "))
posi = int(input("Enter position : "))
lst.insert(posi,user_input)
print()
print(lst)


