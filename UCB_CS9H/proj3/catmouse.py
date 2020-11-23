import argparse

from tkinter import *

from libs.Arena import Arena
from libs.Vector import *
from libs.Color import *
from libs.Turtle import Turtle

from Cat import Cat
from Mouse import Mouse
from Statue import Statue

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

    # YOUR CODE HERE
    cat_radius = 100.0
    cat_angle = 35.0
    mouse_angle = -396.0
    
    Turtle.origin = Vector(400, 300)
    Turtle.m = 50.0

    # TODO: Create your instance for Statue, Cat and Mouse here
    statue = Statue(Turtle.origin, 0)
    mouse = Mouse(Turtle.origin + Vector(0, -50).rotate(mouse_angle), 0)
    cat = Cat(Turtle.origin + Vector(0, cat_radius/2).rotate(cat_angle), 0, mouse=mouse)

    # END OF YOUR CODE

    #########################################
    # DO NOT CHANGE ANY CODE BELOW THIS LINE
    #########################################

    arena.add(statue)
    arena.add(cat)
    arena.add(mouse)
    if args.no_gui:
    	arena.run()
    tk.mainloop()
