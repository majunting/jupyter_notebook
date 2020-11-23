# YOUR CODE HERE
from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *

class Statue(Turtle):
    """docstring for Statue"""
    def __init__(self, position, heading, fill=blue, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
    def getshape(self):
        forward = unit(self.heading)
        return [self.position + (forward*self.m).rotate(x) for x in range(0, 360)]