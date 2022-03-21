from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 40
        self.weapon = Weapon("sword", 40)


    def attack(self, dinosaur):
        print(f'{self.name} attacks {dinosaur.name} with their {self.weapon.name} for {self.weapon.attack_power} points of damage!')
