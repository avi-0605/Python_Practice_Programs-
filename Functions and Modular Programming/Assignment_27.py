import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a,b)
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"The LCM of ",a,"and ",b,"is ",lcm(a,b))
