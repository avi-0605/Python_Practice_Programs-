#Property Decorators Create a class that uses @property to control getting and setting of a private attribute.
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute (by convention)

    @property
    def name(self):
        """Getter method using @property."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter method using @name.setter."""
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            print("Invalid name. Please enter a valid string.")

    @name.deleter
    def name(self):
        """Deleter method using @name.deleter."""
        print(f"Deleting name '{self._name}'")
        self._name = None

# Example usage:
person = Person("Alice")
print("Name:", person.name)  
person.name = "Bob"         
print("Updated Name:", person.name)
person.name = ""            
print("Name after invalid update:", person.name)
print("Name after deletion:", person.name)
