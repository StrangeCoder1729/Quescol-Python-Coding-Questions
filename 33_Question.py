# Q33). Python Program to convert Decimal number to Octal number.



def octal(num):
    
    oct = 1
    rev = 0
    i =1
    while(num > 0):

        oct = num % 8
        rev = rev + (oct*i)
        num = num //8
        i = i*10

    print(rev)



num = int(input("Enter decimal number : "))
octal(num)