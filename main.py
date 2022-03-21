# (/5 points): As a developer, I want to make at least 7 commits with good, descriptive messages.

# (/5 points): As a developer, I want to make a class for each of the following: Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

# (/10 points): As a developer, I want a Robot to have a name, health, and a Weapon (this needs to be its own class and object) with a name (i.e. sword) and attack power.

# (/10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.

# (/10 points): As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values to all the objects.

# (/10 points): As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd (the Fleet and Herd must use a List to store the objects).

# (/10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur to have the ability to attack a Robot on a Battlefield.

# (/10 points): As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) when another Robot/Dinosaur successfully attacks it.

# (/10 points): As a developer, I want the battle to conclude once either all the robots in the Fleet have their health points reach zero or all of the dinosaurs in the Herd have their health points reach zero.

# Bonus Points:

# (/5 points): As a developer, I want a Robot to have the ability to choose from a List of different weapons that will be then assigned as its own weapon.

# (/5 points): As a developer, I want a Dinosaur to have the ability to choose its attack name from a tuple of different attack names before attacking a Robot in battle.

# (/2 points): As a developer, I want a Robot to have a power level and a Dinosaur to have an energy, which will decrease by 10 every time they attack.

from battlefield import Battlefield

play_game = Battlefield()

play_game.run_game()