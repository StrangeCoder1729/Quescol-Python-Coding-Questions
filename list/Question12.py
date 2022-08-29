# Q12). Python Program to calculate length of an array.


lst = []
n = int(input("Enter n : "))

counting = 0
for i in range(0,n):
    user_input = int(input("Enter Number {} : ".format(i+1)))
    lst.append(user_input)
    counting += 1

print("The length of the array is {}".format(counting))
