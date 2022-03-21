from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.power = 100
        self.health = 40
        self.weapon = Weapon("Error", 404)
        self.weapon.list = [Weapon("Space Sword", 40), Weapon("Space Laser", 30), Weapon("Space Punch", 35)]


    def attack(self, dinosaur):
        self.choose_weapon()
        print(f'{self.name} attacks {dinosaur} with their {self.weapon.name} for {self.weapon.attack_power} points of damage!')
    
    def choose_weapon(self):
        for each in self.weapon.list:
            print(each.name)
        wep_choice = input("What weapon would you like to use?")
        for each in self.weapon.list:
            if each.name == wep_choice:
                self.weapon = each