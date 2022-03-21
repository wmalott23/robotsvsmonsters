from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = input("Name your first robot to enter the fleet")
        robot_two = input("Name a second robot to enter your fleet")
        robot_three = input("Name a third robot to enter your fleet")
        self.robots.append(Robot(robot_one), Robot(robot_two), Robot(robot_three))
        print(f'Your robot fleet is {self.robots}')

