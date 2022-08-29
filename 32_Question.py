# Q32). Python Program to Convert Decimal Number into Binary.

def binary(num):
    temp = 0
    bina = 0
    rev = 0
    i  = 1
    while(num > 0):
        # print(f"Number : {num}")
        bina = num % 2
        # print(bina)
        rev = rev + (bina*i)
        # print(rev)
        num = num // 2
       
        i = i*10
    # print(rev)




deci = int(input("Enter Decimal number : "))
binary(deci)