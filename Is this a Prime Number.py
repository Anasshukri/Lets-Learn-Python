prime = bool

while prime is not True:
    j = int(input("Insert a Prime Number: "))

    if j == 2 or j == 3:
        prime = True
        print("It is a Prime Number!")
        break
    else:
        if j % 2 and j % 3 is not 0:
            prime = True
            print("It is a Prime Number!")

        else:
            prime = False
            print("It's not a Prime Number")
