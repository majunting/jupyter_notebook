import argparse

from tkinter import *

from libs.Arena import Arena
from libs.Vector import *
from libs.Color import *
from libs.Turtle import Turtle

from Cat import Cat
from Mouse import Mouse
from Statue import Statue
from globalVariables import *
import updatetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Project 3: Turtle Behavior')
    parser.add_argument('--no-gui', action='store_true')
    args = parser.parse_args()

    tk = Tk()
    if args.no_gui:
        arena = Arena(tk, verbose=True, gui=False)
        arena.runtime_period = 0
    else:
        arena = Arena(tk)
    arena.pack()

    #########################################
    # DO NOT CHANGE ANY CODE ABOVE THIS LINE
    #########################################

    # # YOUR CODE HERE
    # cat_radius = 100.0
    # cat_angle = 35.0
    # mouse_angle = -396.0
    
    # Turtle.origin = Vector(400, 300)
    # Turtle.m = 50.0

    # # TODO: Create your instance for Statue, Cat and Mouse here
    # statue = Statue(Turtle.origin, 0)
    # mouse = Mouse(Turtle.origin + Vector(0, -50).rotate(mouse_angle), 0)
    # cat = Cat(Turtle.origin + Vector(0, cat_radius/2).rotate(cat_angle), 0, mouse=mouse)

    # # END OF YOUR CODE
    radius = 1
    '''
    # case 1
    mouse_angle = 396.000
    mouse_heading = mouse_angle - 90
    cat_angle = 35.000
    cat_heading = cat_angle - 90
    cat_radius = 1.000
    '''

    # case 2
    mouse_angle = -57.000
    mouse_heading = mouse_angle - 90
    cat_angle = 0.000
    cat_heading = cat_angle - 90
    cat_radius = 3.200

    '''
    # case 3
    mouse_angle = 45.000
    mouse_heading = mouse_angle - 90
    cat_angle = 0.1000
    cat_heading = cat_angle - 90
    cat_radius = 8.100
    '''

    '''
    # case 4
    mouse_angle = 240.000
    mouse_heading = mouse_angle - 90
    cat_angle = 150.000
    cat_heading = cat_angle - 90
    cat_radius = 8.100
    '''

    '''
    # case 5
    mouse_angle = -57.000
    mouse_heading = mouse_angle - 90
    cat_angle = 0.000
    cat_heading = cat_angle - 90
    cat_radius = 4.000
    # stoptime = 30*10**3
    '''

    statue = Statue(Vector(200, 200), 0, radius*100)
    mouse = Mouse(Vector(200, 200), mouse_heading, radius*100, 1, mouse_angle, arena)
    cat = Cat(Vector(200, 200),cat_heading, radius*100, cat_radius*100, 1.25, 1, cat_angle, mouse_angle, mouse, arena, updatetime.callback())

    #########################################
    # DO NOT CHANGE ANY CODE BELOW THIS LINE
    #########################################

    arena.add(statue)
    arena.add(cat)
    arena.add(mouse)
    if args.no_gui:
    	arena.run()
    tk.mainloop()
