#Q12). Write a program in Python to swap two numbers using third variable?


def prime(num):
    isprime = True
    for i in range(2,num):
        if(num % i == 0):
            isprime = False
            break
    if(isprime == True):
        return num
    

num = int(input("Enter number : "))
print("Prime factors :-")
for i in range(2, num):
    if(prime(i) == None):
        continue
    if(num % i == 0):
        print(prime(i))
    

