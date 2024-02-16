class Student:
    def __init__(self, name, age):
        self._name = name  # Private attribute for name
        self._age = age  # Private attribute for age

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, age):
        self._age = age


# Demonstration of usage
student = Student("Alice", 20)

# Accessing attributes using getter methods
print("Student name:", student.get_name())  # Output: Student name: Alice
print("Student age:", student.get_age())  # Output: Student age: 20

# Using setter methods to update attributes
student.set_name("Bob")
student.set_age(22)

# Accessing attributes after update
print("Updated student name:", student.get_name())  # Output: Updated student name: Bob
print("Updated student age:", student.get_age())