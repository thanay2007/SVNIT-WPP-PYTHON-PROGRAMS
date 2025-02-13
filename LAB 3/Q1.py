def digital_root(n):
    while n > 9:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        n = sum_digits 
    return n

while(True):
    n = int(input("Enter a number : "))
    dr = digital_root(n)
    print("Digital root:",dr)
    a = input("Do you wish to continue (y/n) : ")
    if a != "y":
        break
