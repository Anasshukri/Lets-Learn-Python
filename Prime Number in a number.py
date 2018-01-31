# Show prime numbers before number

j = int(input("Insert a number: "))

for i in range(1, j + 1):

    if i is not 1:
        if i == 2:
            print("2 is a Prime Number")
        if i == 3:
            print("3 is a Prime Number")
        if i % 2 is not 0:
            if i % 3 is not 0:
                print(i, "is a Prime Number")
                i = i + 1






