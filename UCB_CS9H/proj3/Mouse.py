# YOUR CODE HERE
from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *

class Mouse(Turtle):
	def __init__(self, position, heading, fill=white, **style):
		Turtle.__init__(self, position, heading, fill=fill, **style)
		self.radius = (self.position - self.origin).length()
		self.theta = (self.m / self.radius) * 180 / pi

	def getnextstate(self):
		p = (self.position - self.origin).rotate(-self.theta)
		return p + self.origin, self.heading