#Design Your Own Class!

# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        print(f"{self.name} protects {self.city} using {self.power}!")

    def fight_crime(self):
        print(f"{self.name} is fighting crime in {self.city} 💥")

# Subclass with inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h 🦸‍♂️")

# Creating objects
hero1 = Superhero("ShadowStrike", "Invisibility", "Gotham")
hero2 = FlyingHero("SkyBlaze", "Fire Control", "Metropolis", 300)

# Using methods
hero1.display_info()
hero1.fight_crime()

hero2.display_info()
hero2.fly()
