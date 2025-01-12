# Prime Factors of a Number Find all prime factors of a given integer (e.g., 12 -> 2, 2, 3).

def prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return factors

num = int(input("Enter a number: "))
print("The prime factors of",num," are: ",prime_factors(num))
