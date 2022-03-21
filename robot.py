from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 40
        self.weapon = Weapon("sword", 40)


    def attack(self, dinosaur):
        print(f'{self.name} attacks {dinosaur} with their {Weapon.name} for {Weapon.attack_power} points of damage!')