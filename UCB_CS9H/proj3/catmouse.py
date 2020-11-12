import argparse

from tkinter import *

from libs.Arena import Arena

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
    cat_radius = ...
    cat_angle = ...
    mouse_angle = ...
    
    # TODO: Create your instance for Statue, Cat and Mouse here
    statue = ...
    mouse = ...
    cat = ...

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
