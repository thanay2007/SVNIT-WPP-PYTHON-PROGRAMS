import math
def sherlock_square(n1,n2):
    perfect_sq = 0
    for i in range (n1+1,n2):
        if (math.sqrt(i).is_integer()):
            perfect_sq +=1
    return perfect_sq

def sherlock_list(n1,n2):
    perfect_list = []
    for i in range (n1+1,n2):
        if (math.sqrt(i).is_integer()):
            perfect_list.append(i)
    return perfect_list

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number : "))
perfect_sq = sherlock_square(n1,n2)
perfect_list = sherlock_list(n1,n2)
print("Number of numbers with perfect square between",n1,"and",n2,"is",perfect_sq,"and the numbers are",perfect_list)
