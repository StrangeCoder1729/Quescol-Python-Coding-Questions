#Q4). Write a program in Python to print the Fibonacci series using iterative method

def fib(n):
    n1 = 0
    n2 = 1
    sum = 0
    i = 0
    print(f"{n1} {n2} ",end='')
    while(i < n):
        
        sum = n1 + n2
        n1 = n2
        n2 = sum
        print(sum,end=' ')
        i+=1




n = int(input("Enter number : "))
fib(n)