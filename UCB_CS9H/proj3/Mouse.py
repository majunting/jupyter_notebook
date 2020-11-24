# # YOUR CODE HERE
# from libs.Turtle import Turtle
# from libs.Vector import *
# from libs.Color import *

# class Mouse(Turtle):
# 	def __init__(self, position, heading, fill=white, **style):
# 		Turtle.__init__(self, position, heading, fill=fill, **style)
# 		self.radius = (self.position - self.origin).length()
# 		self.theta = (self.m / self.radius) * 180 / pi

# 	def getnextstate(self):
# 		p = (self.position - self.origin).rotate(-self.theta)
# 		return p + self.origin, self.heading

from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *
from libs.Arena import Arena
import math

class Mouse(Turtle):  # Inherit behavior from Turtle
    def __init__(self, position, heading, radius, mouse_speed, mouse_angle, arena, fill=grey, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        # heading is the angle of the turtle's direction
        self.radius = radius
        self.mouse_speed = mouse_speed
        self.mouse_angle = mouse_angle
        self.heading = self.mouse_angle - 90
        #self.position = self.position + unit(self.heading + 90)*self.radius
        self.position = self.position + unit(self.heading + 90)*self.radius
        self.arena = arena
        # assume the heading is the direction that the tutle is facing

    def getnextstate(self):
        self.heading = self.heading - 360/(2*math.pi*self.radius)
        self.position = self.position + unit(self.heading)*self.mouse_speed
        self.arena.new_angle_label.config(text = 'MouseAngle [°]: ' + str(round((self.heading + 90)%360,3)))
        return self.position, self.heading