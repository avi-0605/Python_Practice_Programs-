# Sum of Digits Compute the sum of digits of an integer using a loop.
def sum_of_digits(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10  
        num //= 10  
    return total_sum

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of digits of {num} is {result}.")
