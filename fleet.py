from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = input("Name your first robot to enter the fleet")
        robot_two = input("Name a second robot to enter your fleet")
        robot_three = input("Name a third robot to enter your fleet")
        rob_obj_one = Robot(robot_one)
        rob_obj_two = Robot(robot_two)
        rob_obj_three = Robot(robot_three)
        self.robots.append(rob_obj_one)
        self.robots.append(rob_obj_two)
        self.robots.append(rob_obj_three)
        print(f'Your robot fleet is {rob_obj_one.name}, {rob_obj_two.name}, {rob_obj_three.name}')