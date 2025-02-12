def utopian_tree(n, initial_height):
    height = initial_height
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:  
            height += 1
    return height

t = int(input("Enter the number of test cases: "))
for i in range(t):
    initial_height = int(input("Enter the initial height of the tree: "))
    n = int(input("Enter the number of growth cycles: "))
    print("The height of the tree after", n, "cycles is:", utopian_tree(n, initial_height))
