#  import math library
import math

print("Let's calculate a hypotenuse using Pythagoras Theorem!")

x = int(input("x side: "))
y = int(input("y side: "))
#  Using math library to use exponent and square root
c = math.pow(x, 2) + math.pow(y, 2)
z = math.sqrt(c)

print("Your hypotenuse is ", z)

