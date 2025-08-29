# Base class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclasses with polymorphic behavior
class Fish(Animal):
    def move(self):
        return "Swimming in the lake"

class Bird(Animal):
    def move(self):
        return " Flying in the sky"

class Dog(Animal):
    def move(self):
        return "work, run on the land"

class Snake(Animal):
    def move(self):
        return "Slithering on land"

# Function demonstrating polymorphism
def show_movement(animal):
    print(animal.move())

# Create objects of different animal types
animals = [Fish(), Bird(), Dog(), Snake()]

# Loop through and demonstrate polymorphism
for animal in animals:
    show_movement(animal)
