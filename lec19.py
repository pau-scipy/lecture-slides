"""
A module for drawing fractals with L-systems, using matplotlib.
Illustrates plotting, dictionaries, strings, loops, functions and a class.
"""

import matplotlib.pyplot as plt
import math


class FractalMover(object):
    """A class that represents the movement of a turtle in 2-d space"""
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        # A dictionary of the correspondence between characters and movement functions
        self.movement = { 'F':self.forward, '+':self.turn_right, '-':self.turn_left }    

    def forward(self):
        self.x = self.x + math.cos(self.direction)
        self.y = self.y + math.sin(self.direction)
        return ( (self.x, self.y) )

    def turn_right(self):
        self.direction = (self.direction - theta) % (2*math.pi)
        return ( (self.x, self.y) )

    def turn_left(self):
        self.direction = (self.direction + theta) % (2*math.pi)
        return ( (self.x, self.y) )



def lsystem():
    """Expand an axiom using the rules, for several iterations"""
    commands = axiom
    for i in range(iterations):
        cs = []
        for c in commands:
            if c in rules:
                cs += rules[c]
            else:
                cs += c
        commands = cs
    return commands

    


def interpret_commands(command_string):
    """Takes a string and converts it into the corresponding x and y locations"""
    x_posns = []
    y_posns = []
    fm = FractalMover(0, 0, 0)
    for c in command_string:
        if c not in rules:
            # look up the correct movement function to use for this character
            move_function = fm.movement[c]
            # apply the function and collect the new x and y locations
            (newx, newy) = move_function()
            x_posns.append(newx)
            y_posns.append(newy)
    return (x_posns, y_posns)


if __name__ == "__main__":

    # sierpinski
    axiom = 'FX+'
    rules = {
       'X': 'YF+XF+Y',
       'Y': 'XF-YF-X'
       }
    theta = math.radians(60)
    iterations = 6

    # dragon
    # axiom = "FX+FX+"
    # rules = {
    #    'X' : 'X+YF',
    #    'Y' : 'FX-Y'
    #    }
    # theta = math.radians(90)
    # iterations = 10

    # Run the l-system to produce a final command string
    command_string = lsystem()
    # Interpret the commands to produce x and y locations showing where we moved
    (x_posns, y_posns) = interpret_commands(command_string)

    plt.plot(x_posns, y_posns, 'b-')
    plt.plot(x_posns, y_posns, 'b.')
    plt.show()
