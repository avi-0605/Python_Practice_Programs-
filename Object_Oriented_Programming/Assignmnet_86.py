#Class** ComplexNumberImplement a class that represents a complex number with real and imaginary parts. Overload addition and subtraction operators (if you want to practice operator overloading in Python).
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

sum_result = c1 + c2
sub_result = c1 - c2

print("Sum:", sum_result)      
print("Difference:", sub_result)  
