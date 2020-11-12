"""DO NOT MODIFY THIS FILE. This file is for demonstration purpose only."""

from tkinter import *                              # Import everything from Tkinter

from libs.Arena import Arena                       # Import our Arena
from libs.Vector import *                          # Import everything from our Vector
from WalkingTurtle import WalkingTurtle            # Import the WalkingTurtle

tk = Tk()                                          # Create a Tk top-level widget
arena = Arena(tk)                                  # Create an Arena widget, arena
arena.pack()                                       # Tell arena to pack itself on screen
arena.add(WalkingTurtle(Vector(200, 200), 0, 1))   # Add a very simple, basic turtle
tk.mainloop()                                      # Enter the Tkinter event loop
