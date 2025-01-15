class MyClass:
    # Regular instance method
    def instance_method(self):
        return f"Called instance method. self={self}"

    # Class method
    @classmethod
    def class_method(cls):
        return f"Called class method. cls={cls}"

    # Static method
    @staticmethod
    def static_method():
        return "Called static method. No self or cls."

# Example usage:
obj = MyClass()

# Calling instance method (requires an object)
print(obj.instance_method())  

# Calling class method (can be called using class or object)
print(MyClass.class_method())  
print(obj.class_method())      

# Calling static method (can be called using class or object)
print(MyClass.static_method()) 
print(obj.static_method())     
