from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to the big battle of dinosaurs and robots!")

    def battle(self):
        dino_total = self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health
        robo_total = self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health
        counter = 1
        while dino_total > 0 and robo_total > 0:
            if counter == 2:
                self.show_dino_opponent_options()
                robo_choice = input("Which robot would like to attack with?")
                for each in self.fleet.robots:
                    if each.name == robo_choice:
                        self.robo_turn(each)
                counter = 1
            elif counter == 1:
                self.show_robo_opponent_options()
                dino_choice = input("Which dino would you like to attack with?")
                for each in self.herd.dinosaurs:
                    if each.name == dino_choice:
                        self.dino_turn(each)
                counter = 2
            dino_total = self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health
            robo_total = self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health
        print("Battle Over!")
        

    def dino_turn(self, dinosaur):
        self.show_dino_opponent_options()
        att_choice = input("Which robo would you like to attack?")
        for each in self.fleet.robots:
            if each.name == att_choice:
                each.health -= dinosaur.attack_power
                dinosaur.energy -= 10
                dinosaur.attack(att_choice)
                if each.health <= 0:
                    each.health = 0
                    print(f'{each.name} now has 0 health left! {each.name} is out of the fight!')
                else:
                    print(f'{each.name} now has {each.health} health left!')
                print(f'{dinosaur.name} now has {dinosaur.energy} energy')


    def robo_turn(self, robot):
        self.show_robo_opponent_options()
        att_choice = input("Which dino would you like to attack?")
        for each in self.herd.dinosaurs:
            if each.name == att_choice:
                robot.attack(att_choice)
                each.health -= robot.weapon.attack_power
                robot.power -= 10
                if each.health <= 0:
                    each.health = 0
                    print(f'{each.name} now has 0 health left! {each.name} is out of the fight!')
                else:
                    print(f'{each.name} now has {each.health} health left!')
                print(f'{robot.name} now has {robot.power} power')

    def show_dino_opponent_options(self):
        for each in self.fleet.robots:
            if each.health > 0:
                print(each.name)

    def show_robo_opponent_options(self):
        for each in self.herd.dinosaurs:
            if each.health > 0:
                print(each.name)

    def display_winners(self):
        dino_total = self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health
        robo_total = self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health
        if dino_total > 0:
            print("Dinos win!")
        if robo_total > 0:
            print("Robots win!")