# Q29). Python program to calculate LCM of given two numbers.

def LCM(num1, num2):
    greater = 0
    if(num1>num2):
        greater = num1
    else:
        greater = num2
    
    while(True):
        if(greater % num1 == 0) and (greater % num2 == 0):
            return greater
        greater +=1
     
            


num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

print(LCM(num1,num2))

