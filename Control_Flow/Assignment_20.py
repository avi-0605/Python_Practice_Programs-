a=int(input("Enter a number : "))
rev=0
org=a
while a>0:
    d=a%10              
    rev=rev*10+d  
    a=a//10             
if org==rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")