# # YOUR CODE HERE
# from libs.Turtle import Turtle
# from libs.Vector import *
# from libs.Color import *

# class Statue(Turtle):
#     """docstring for Statue"""
#     def __init__(self, position, heading, fill=blue, **style):
#         Turtle.__init__(self, position, heading, fill=fill, **style)
#     def getshape(self):
#         forward = unit(self.heading)
#         return [self.position + (forward*self.m).rotate(x) for x in range(0, 360)]

from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *

class Statue(Turtle):
    def __init__(self, position, heading, radius):
        Turtle.__init__(self, position, heading)
        self.radius = radius

    def getshape(self):
        # Return a list of vectors giving the polygon for this turtle.
        statue_pts = []
        for i in range(360):
            forward = unit(i)
            statue_pts = statue_pts + [self.position + forward * self.radius]
        return statue_pts