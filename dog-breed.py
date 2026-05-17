# Dog class with:
# 1 class variable
# 2 instance variables

class Dog:
    # Class variable (shared by all objects)
    animal = "Dog"

    # Constructor
    def __init__(self, breed, name):
        # Instance variables
        self.breed = breed
        self.name = name

    # Method to display details
    def display_details(self):
        print("Animal Type:", Dog.animal)
        print("Breed:", self.breed)
        print("Name:", self.name)
        print()


# Creating objects of two different breeds
dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("German Shepherd", "Max")

# Displaying details
dog1.display_details()
dog2.display_details()