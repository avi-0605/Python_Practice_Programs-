# Create a Simple Calculator (Functions)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: Division by zero is not allowed"
    else:
        return a/b


print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4): "))
n1= int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if choice==1:
    print(n1,"+",n2,"=",add(n1,n2))
elif choice==2:
    print(n1,"-",n2,"=",subtract(n1,n2))
elif choice == '3':
    print(n1,"*",n2,"=",multiply(n1,n2))
elif choice == '4':
    print(n1,"/",n2,"=",divide(n1,n2))
