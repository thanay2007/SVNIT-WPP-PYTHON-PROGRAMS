names_list = []
n = int(input("Enter a number: "))

for i in range(0, n):
    name = input("Enter a name: ")
    if (len(name) > 15):
        print("Dont enter a name with more than 15 charecters")
        break
    names_list.append(name)

for i in range(0, n):
    print("Reverse name:", names_list[i][::-1])
