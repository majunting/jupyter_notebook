# YOUR CODE HERE
from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *
from Mouse import Mouse
from math import acos

# class Cat(Turtle):
# 	def __init__(self, position, radius, heading, speed, fill=white, **style):
# 		Turtle.__init__(self, position, heading, fill=fill, **style)
# 		self.speed = speed
# 		self.radius = radius

# 	# def getshape(self):

# 	def get_next_state(self):
# 		return self.position, self.radius, self.heading

# 	def set_state(self, state):
# 		self.position, self.radius, self.heading = state

class Cat(Turtle):
    """docstring for Cat"""
    def __init__(self, position, heading, mouse, fill=red, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        self.mouse = mouse
        self.radius = (self.position - self.origin).length()
        self.theta = (self.m * 1.25 / self.radius) * 180 / pi

    def getnextstate(self):
        p = (self.position - self.origin).rotate(-self.theta)
        cat_angle = (self.position - self.origin).direction()
        mouse_angle = (self.mouse.position - self.origin).direction()
        phi = acos(self.m / self.radius) * 180 / pi
        diff = mouse_angle - cat_angle
        if diff > 270:
            diff = 360 - diff
        next_angle_diff = ((self.mouse.position - self.origin).rotate(-self.mouse.theta)).direction() - p.direction()
        print (next_angle_diff)
        if int(self.radius) == int(self.m) and diff / abs(diff) < next_angle_diff / abs(next_angle_diff) and abs(diff - next_angle_diff) <= 50:
            print ("Mouse caught!")
            Mouse.getnextstate = Turtle.getnextstate
            Cat.getnextstate = Turtle.getnextstate
        print ("cat_angle: %f \nmouse_angle: %f \nangle_difference: %f \ncat_radius: %f" % (cat_angle, mouse_angle, diff, self.radius))
        if abs(diff) <= phi and not self.radius <= self.m:
            u = unit((self.position - self.origin).direction())
            new_pos = (self.radius - self.m) * u
            self.radius -= self.m
            if self.radius < self.m:
                self.radius = self.m
                new_pos = self.m * u
            self.theta = (self.m * 1.25 / self.radius) * 180 / pi
            print ('position:', new_pos.x, new_pos.y, "\n")
            return new_pos + self.origin, self.heading
        else:
            print ('position:', p.x, p.y, "\n")
            return p + self.origin, self.heading