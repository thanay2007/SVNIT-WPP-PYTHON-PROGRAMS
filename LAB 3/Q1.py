def digital_root(n):
    while n > 9:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        n = sum_digits 
    return n

n = int(input("Enter a number : "))
n = digital_root(n)
print("Digital root: ",n)
