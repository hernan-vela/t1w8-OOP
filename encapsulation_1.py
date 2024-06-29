class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.__age = age # Double underscore for Private attribute
        self.__email = email # Double underscore for Private attribute
    
    # Getter for age (function created to change and fetch a private attribute)
    def get_age(self):
        return self.__age
    
    # Setter for age (function created to change and fetch a private attribute)
    def set_age(self, age):
        self.__age = age

    # Getter for email (function created to change and fetch a private attribute)
    def get_email(self):
        return self.__email
    
    # Setter for email (function created to change and fetch a private attribute)
    def set_email(self, email):
        self.__email = email
    
    # Show all info, including encapsulated info
    def display_info(self):
        return f"Name: {self.name}, Age: {self.__age}, Email: {self.__email}"
    
# Create an object
person1 = Person("John Doe", 30, "john.doe@example.com")

# Accessing and modifying age using getter and setter
print(person1.get_age())
person1.set_age(31)
print(person1.get_age())

print(person1.get_email())
person1.set_email("john.new@example.com")
print(person1.get_email())

print(person1.display_info())

