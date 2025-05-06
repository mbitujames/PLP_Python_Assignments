#Polymorphism Challenge

class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# List of animals
animals = [Dog(), Bird(), Fish()]

# Polymorphic behavior
for animal in animals:
    animal.move()
