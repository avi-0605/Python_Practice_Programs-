# Sum of N Natural Numbers
a=int(input("Enter a number : "))
sum=0
for i in range(1,a+1):
    sum+=i
print("Sum of first",a,"natural numbers is",sum)