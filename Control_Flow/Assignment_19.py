#Sum of Even and Odd Numbers Separately
a=int(input("Enter a number : "))
sum_e=0
sum_o=0
for i in range(1,a+1):
    if i%2==0:
        sum_e+=i
    else:
        sum_o+=i
print("Sum of first",a,"even natural numbers is",sum_e)
print("Sum of first",a,"odd natural numbers is",sum_o)
