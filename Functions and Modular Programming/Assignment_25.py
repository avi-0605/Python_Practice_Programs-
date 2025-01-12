# Write a function fibonacci(n) that returns a list of the first n Fibonacci numbers.
def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]  
a = int(input("Enter a number: ")) 
print(fibonacci(a))
    
