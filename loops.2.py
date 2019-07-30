item = ""
while item != "quit":
    print("Enter an item to check the price: ")
    item = input()


    if item == "pizza":
        print("$3 per slice")
    elif item == "oppai":
        print("Free")  
    else:
        print("We don't have that")    