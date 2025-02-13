def is_fibonacci(n):
    a = 0
    b = 1
    while b <= n:
        if b == n:
            return True  
        a = b
        b = a + b 
    return False

while(True):
    num = int(input("Enter a number: "))

    if is_fibonacci(num) == True:
        print(num, "is a fibonacci number.")
    else:
        print(num, "is not a Fibonacci number.")

    a = input("Do you wish to continue (y/n) : ")
    if a != "y":
        break
