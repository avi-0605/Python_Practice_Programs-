# Perfect Number Check if an integer is a perfect number. A perfect number equals the sum of its proper divisors (e.g., 6 = 1+2+3).
def is_perfect_number(num):
    if num <= 0:
        return False
    sum_of_divisors = 0
    for i in range(1, num): 
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a Perfect Number.")
else:
    print(f"{number} is not a Perfect Number.")