from string import ascii_lowercase

while (True):
    sentence = input("Enter a sentence: ")
    list = []

    for i in sentence: 
        if i.lower().isalpha():
            if i.lower() not in list:
                list.append(i.lower())

    if len(list) == 26:
        print("The sentence is a panagram")
    else:
        print("The sentence is not a panagram")

    a = input("Do you want to continue (y/n) : ")
    if a != "y":
        break
