"""
@Author: Andrew Bohlman
Creates a virtual x/y plane to move a marker around on
"""


import turtle
import re
import keyboard


class Plane:
    x = 0
    y = 0

    def __init__(self):
        x = 0
        y = 0

    def initialize_plane(self): # Only used in testing version
        turtle.up()
        turtle.forward(250)
        turtle.right(90)
        turtle.forward(250)
        turtle.right(90)
        turtle.down()
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(500)
        turtle.up()
        turtle.right(90)
        turtle.forward(500)
        turtle.right(180)

    def move_to_point(self, x, y):  # Takes the shortest path to the target point
        turtle.speed(100)
        x_distance = x - self.x
        y_distance = y - self.y
        max_dist = max(x_distance, y_distance)
        min_dist = min(x_distance, y_distance)
        ratio = max_dist / min_dist
        ratio = abs(ratio)
        if y_distance > x_distance:
            for i in range(x_distance):
                if y_distance < 0:
                    self.move_down(ratio)
                else:
                    self.move_up(ratio)

                if x_distance < 0:
                    self.move_left(1)
                else:
                    self.move_right(1)
        else:
            for i in range(y_distance):
                if y_distance < 0:
                    self.move_down(1)
                else:
                    self.move_up(1)

                if x_distance < 0:
                    self.move_left(ratio)
                else:
                    self.move_right(ratio)

    def move_corner(self, x, y):    # Takes a right angle to the target point
        x_distance = x - self.x
        y_distance = y - self.y
        if y_distance < 0:
            y_distance = abs(y_distance)
            self.move_down(y_distance)
        else:
            self.move_up(y_distance)

        if x_distance < 0:
            x_distance = abs(x_distance)
            self.move_left(x_distance)
        else:
            self.move_right(x_distance)

    """
    def move_arc(self, x, y):   # Takes a curved path to the target point
        print("arc start")
        turtle.speed(100)
        x_distance = x - self.x
        y_distance = y - self.y
        if y_distance > x_distance:
            x_speed = 1
            y_speed = y_distance / 3
            for i in range(x_distance):
                if y_distance < 0:
                    self.move_down(y_speed)
                else:
                    self.move_up(y_speed)

                if x_distance < 0:
                    self.move_left(x_speed)
                else:
                    self.move_right(x_speed)
                x_speed = x_speed + 1
                y_speed = y_speed - 1
        else:
            x_speed = x_distance / 3
            y_speed = 1
            for i in range(x_distance):
                if y_distance < 0:
                    self.move_down(y_speed)
                else:
                    self.move_up(y_speed)

                if x_distance < 0:
                    self.move_left(x_speed)
                else:
                    self.move_right(x_speed)
                y_speed = y_speed + 1
                x_speed = x_speed - 1
        print("arc complete")
    """

    def move_up(self, y_dist):  # Replace with motor stuff
        if self.y < 500:
            turtle.seth(90)
            turtle.forward(y_dist)
            self.y = self.y + y_dist

    def move_down(self, y_dist):    # Replace with motor stuff
        if self.y > 0:
            turtle.seth(270)
            turtle.forward(y_dist)
            self.y = self.y - y_dist

    def move_left(self, x_dist):    # Replace with motor stuff
        if self.x > 0:
            turtle.seth(180)
            turtle.forward(x_dist)
            self.x = self.x - x_dist

    def move_right(self, x_dist):   # Replace with motor stuff
        if self.x < 500:
            turtle.seth(0)
            turtle.forward(x_dist)
            self.x = self.x + x_dist

    def draw_rectangle(self, x, y):
        print("Drawing rect")
        orig_x = self.x
        orig_y = self.y
        self.move_corner(x, y)
        self.move_corner(orig_x, orig_y)


class Pen:
    pen_state = 'up'

    def pen_up(self):
        if self.pen_state == 'down':
            turtle.up()
            self.pen_state = 'up'

    def pen_down(self):
        if self.pen_state == 'up':
            turtle.down()
            self.pen_state = 'down'


turtle = turtle.Turtle()
screen = turtle.getscreen()
turtle.speed(10)
test_plane = Plane()
test_plane.initialize_plane()
pen_ob = Pen()
while True:
    command = input("Enter command: ")
    command = re.split(' ', command)
    mode = command[0]
    print(mode)
    if mode.lower() == 'rectangle':
        pen_ob.pen_down()
        x = command[1]
        x = int(x)
        y = command[2]
        y = int(y)
        test_plane.draw_rectangle(x, y)
    elif mode.lower() == 'triangle':
        pen_ob.pen_down()
        x = command[1]
        x = int(x)
        y = command[2]
        y = int(y)
        test_plane.draw_triangle()
    elif mode.lower() == 'circle':
        pen_ob.pen_down()
        x = command[1]
        x = int(x)
        y = command[2]
        y = int(y)
        # test_plane.draw_circle()
    elif mode.lower() == 'move':
        pen_ob.pen_up()
        x = command[1]
        x = int(x)
        y = command[2]
        y = int(y)
        if x == 0 and y == 0:
            test_plane.move_to_point(x, y)
            print('break')
            break
        test_plane.move_corner(x, y)
    elif mode.lower() == 'draw':
        pen_ob.pen_down()
        x = command[1]
        x = int(x)
        y = command[2]
        y = int(y)
        if x == 0 and y == 0:
            test_plane.move_to_point(x, y)
            print('break')
            break
        test_plane.move_to_point(x, y)
    elif mode.lower() == 'arc':
        pen_ob.pen_down()
        x = command[1]
        x = int(x)
        y = command[2]
        y = int(y)
        if x == 0 and y == 0:
            test_plane.move_arc(x, y)
            print('break')
            break
        test_plane.move_arc(x, y)
    elif mode.lower() == 'manual':
        turtle.speed(50)
        print("-Entering manual control-")
        while True:
            print("X: " + str(test_plane.x) + "     Y: " + str(test_plane.y))
            if keyboard.is_pressed('w'):
                test_plane.move_up(1)
            elif keyboard.is_pressed('s'):
                test_plane.move_down(1)
            if keyboard.is_pressed('d'):
                test_plane.move_right(1)
            elif keyboard.is_pressed('a'):
                test_plane.move_left(1)
            if keyboard.is_pressed('space'):
                if pen_ob.pen_state == 'up':
                    pen_ob.pen_down()
                else:
                    pen_ob.pen_up()
            if keyboard.is_pressed('esc'):
                break

screen.mainloop()
