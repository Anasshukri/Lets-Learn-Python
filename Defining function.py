name = input("What is your name?\n")


def greet(x):
    print("Hello, " + x + ".")
    condition = input("How are you today?\n")
    if condition is "good" or "Good":
        print("Good!")
    else:
        print("Do something!")

greet(name)
