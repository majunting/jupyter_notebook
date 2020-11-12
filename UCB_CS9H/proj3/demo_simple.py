"""DO NOT MODIFY THIS FILE. This file is for demonstration purpose only."""

from tkinter import *                      # Import everything from Tkinter

from libs.Arena import Arena               # Import our Arena
from libs.Vector import *                  # Import everything from our Vector
from libs.Turtle import Turtle             # Import the Turtle

tk = Tk()                                  # Create a Tk top-level widget
arena = Arena(tk)                          # Create an Arena widget, arena
arena.pack()                               # Tell arena to pack itself on screen
arena.add(Turtle(Vector(200, 200), 0))     # Add a very simple, basic turtle
tk.mainloop()                              # Enter the Tkinter event loop
