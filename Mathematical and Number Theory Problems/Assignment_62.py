# Strong Number Check if an integer is a strong number. A strong number is one whose sum of factorials of digits equals the number (e.g., 145 = 1! + 4! + 5!).
import math
def is_strong_number(num):
    sum_of_factorials = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += math.factorial(digit)
        temp //= 10
    return sum_of_factorials == num
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is not a Strong Number.")