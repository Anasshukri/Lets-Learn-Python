n = int(input("n rows:"))
for i in range(0, n):    # loop will execute from 1 to 4(n-1)
    for j in range(0, i+1):
        print("*", end="")
    print()
