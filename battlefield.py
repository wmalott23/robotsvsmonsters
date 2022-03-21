from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_welcome(self):
        print("Welcome to the big battle of dinosaurs and robots!")

    def battle(self):
            counter = 1
            if counter % 2 == 0:
                self.show_dino_opponent_options()
                robo_choice = input("Which robot would like to attack with?")
                for robo_choice in self.fleet.robots:
                    self.robo_turn(robo_choice)
            elif counter % 2 != 0:
                self.show_robo_opponent_options()
                dino_choice = input("Which dino would you like to attack with?")
                for dino_choice in self.herd.dinosaurs:
                    self.dino_turn(dino_choice)
            counter += 1

    def dino_turn(self, dinosaur):
        self.show_dino_opponent_options()
        att_choice = input("Which robo would you like to attack?")
        for att_choice in self.fleet.robots:
            att_choice.health -= dinosaur.attack_power
        dinosaur.attack()

    def robo_turn(self, robot):
        self.show_robo_opponent_options()
        att_choice = input("Which dino would you like to attack?")
        for att_choice in self.herd.dinosaurs:
            att_choice.health -= robot.attack_power
        robot.attack()

    def show_dino_opponent_options(self):
        for each in self.fleet.robots:
            if each.health >= 0:
                print(each.name)

    def show_robo_opponent_options(self):
        for each in self.herd.dinosaurs:
            if each.health >= 0:
                print(each.name)

    def display_winners(self):
        pass

herd = Battlefield()

herd.battle()