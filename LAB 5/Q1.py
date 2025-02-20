def max_xor(start, end):
    for i in range(start, end + 1):
        for j in range(i, end + 1): 
            result = i ^ j
            print(i,"xor",j,"=", result)

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
max_xor(a,b)
