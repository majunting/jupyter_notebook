# YOUR CODE HERE
class Cat(Turtle):
	def __init__(self, position, radius, heading, speed, fill=white, **style):
		Turtle.__init__(self, position, heading, fill=fill, **style)
		self.speed = speed
		self.radius = radius

	# def getshape(self):

	def get_next_state(self):
		return self.position, self.radius, self.heading

	def set_state(self, state):
		self.position, self.radius, self.heading = state