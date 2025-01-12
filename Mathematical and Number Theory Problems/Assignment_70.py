#Sieve of Eratosthenes Implement the Sieve of Eratosthenes to find all prime numbers up to n.
def sieve_of_eratosthenes(n):
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

# Example usage:
n = int(input("Enter a number: "))
print(f"Prime numbers up to ",n," are: ",sieve_of_eratosthenes(n))
