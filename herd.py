from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one_name = input("what name would you like to give your dinosaur?")
        dino_one_att = input("How strong would you like them to be?")
        dino_two_name = input("What name would you like to give your second dinosaur?")
        dino_two_att = input("How strong would you like them to be?")
        dino_three_name = input("Type in Lil' Foot")
        dino_three_att = input("Type in 100")
        self.dinosaurs.append(Dinosaur(dino_one_name, dino_one_att))
        self.dinosaurs.append(Dinosaur(dino_two_name, dino_two_att))
        self.dinosaurs.append(Dinosaur(dino_three_name, dino_three_att))

        
        print(f'Your herd is made up of {self.dinosaurs[0].name}, {self.dinosaurs[1].name}, and the ultra powerful {self.dinosaurs[2].name}!')
