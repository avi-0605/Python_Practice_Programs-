#Power Function**
def power(base, exponent):
    result=1
    for i in range(1,exponent+1):
        result*=base          
    return result               
b = int(input("Enter the base: "))
e = int(input("Enter the exponent: "))
print(power(b,e))

    