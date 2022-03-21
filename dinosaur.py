class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = 50
        self.energy = 100
        self.att_list = ["Tail whip", "Body Slam", "Stomp", "Hyper Beam"]
        self.att = "error"

    def attack(self, robot):
        self.att_choose()
        print(f'{self.name} attacks {robot} with a {self.att} and does {self.attack_power} points of damage!')

    def att_choose(self):
        for each in self.att_list:
            print(each)
        attack_choice = input("What attack would you like to use?")
        for each in self.att_list:
            if each == attack_choice:
                self.att = each