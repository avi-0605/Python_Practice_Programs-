#LCM of a Range Compute the LCM of all numbers in a given range [1..n].
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def lcm_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result
n = int(input("Enter a number: "))
print(f"The LCM of numbers from 1 to {n} is {lcm_range(n)}")
