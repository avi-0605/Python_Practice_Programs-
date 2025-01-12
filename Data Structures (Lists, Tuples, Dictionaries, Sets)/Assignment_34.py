# Sum and Average of a List Prompt the user for a list of numbers. Calculate and print the sum and average.

numbers=input("Enter numbers: ").split()
number=[int(n) for n in numbers]
n_sum=sum(number)
n_avg=n_sum/len(numbers)
print("Sum:",n_sum)
print("Average:",n_avg)
