# Base class
class Superhero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.__is_fighting = False  # Encapsulation: private attribute
    
    def introduce(self):
        return f"I am {self.name}!"
    
    def use_power(self):
        return f"{self.name} uses {self.powers}!"
    
    def start_fight(self):
        if not self.__is_fighting:
            self.__is_fighting = True
            return f"{self.name} is now fighting crime!"
        return f"{self.name} is already fighting!"
    
    def end_fight(self):
        if self.__is_fighting:
            self.__is_fighting = False
            return f"{self.name} has stopped fighting."
        return f"{self.name} wasn't fighting."
    
    def is_fighting(self):
        return self.__is_fighting

# Subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, powers, max_speed):
        super().__init__(name, secret_identity, powers)
        self.max_speed = max_speed
    
    # Polymorphism: override method
    def use_power(self):
        return f"{self.name} soars through the sky at {self.max_speed} mph!"
    
    def fly(self):
        return f"{self.name} takes to the skies!"

# Example usage
hero = Superhero("Shadow", "Alex Morgan", "invisibility")
flying_hero = FlyingSuperhero("Skyhawk", "Jamie Chen", "flight and super strength", 500)

print(hero.introduce())
print(hero.start_fight())
print(hero.end_fight())
print(flying_hero.use_power())  # Polymorphic behavior
print(flying_hero.fly())
print(flying_hero.start_fight())  # Inherited method
