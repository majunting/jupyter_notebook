# # YOUR CODE HERE
# from libs.Turtle import Turtle
# from libs.Vector import *
# from libs.Color import *
# from Mouse import Mouse
# from math import acos

# # class Cat(Turtle):
# # 	def __init__(self, position, radius, heading, speed, fill=white, **style):
# # 		Turtle.__init__(self, position, heading, fill=fill, **style)
# # 		self.speed = speed
# # 		self.radius = radius

# # 	# def getshape(self):

# # 	def get_next_state(self):
# # 		return self.position, self.radius, self.heading

# # 	def set_state(self, state):
# # 		self.position, self.radius, self.heading = state

# class Cat(Turtle):
#     """docstring for Cat"""
#     def __init__(self, position, heading, mouse, fill=red, **style):
#         Turtle.__init__(self, position, heading, fill=fill, **style)
#         self.mouse = mouse
#         self.radius = (self.position - self.origin).length()
#         self.theta = (self.m * 1.25 / self.radius) * 180 / pi

#     def getnextstate(self):
#         p = (self.position - self.origin).rotate(-self.theta)
#         cat_angle = (self.position - self.origin).direction()
#         mouse_angle = (self.mouse.position - self.origin).direction()
#         phi = acos(self.m / self.radius) * 180 / pi
#         diff = mouse_angle - cat_angle
#         if diff > 270:
#             diff = 360 - diff
#         next_angle_diff = ((self.mouse.position - self.origin).rotate(-self.mouse.theta)).direction() - p.direction()
#         print (next_angle_diff)
#         if int(self.radius) == int(self.m) and diff / abs(diff) < next_angle_diff / abs(next_angle_diff) and abs(diff - next_angle_diff) <= 50:
#             print ("Mouse caught!")
#             Mouse.getnextstate = Turtle.getnextstate
#             Cat.getnextstate = Turtle.getnextstate
#         print ("cat_angle: %f \nmouse_angle: %f \nangle_difference: %f \ncat_radius: %f" % (cat_angle, mouse_angle, diff, self.radius))
#         if abs(diff) <= phi and not self.radius <= self.m:
#             u = unit((self.position - self.origin).direction())
#             new_pos = (self.radius - self.m) * u
#             self.radius -= self.m
#             if self.radius < self.m:
#                 self.radius = self.m
#                 new_pos = self.m * u
#             self.theta = (self.m * 1.25 / self.radius) * 180 / pi
#             print ('position:', new_pos.x, new_pos.y, "\n")
#             return new_pos + self.origin, self.heading
#         else:
#             print ('position:', p.x, p.y, "\n")
#             return p + self.origin, self.heading


import argparse

from tkinter import *

from libs.Arena import Arena                      # Import our Arena

from libs.Turtle import Turtle
from libs.Vector import *
from libs.Color import *
from Mouse import *
import math
#from tkinter import *

class Cat(Turtle):
    def __init__(self, position, heading, radius, cat_radius, cat_cycle_speed, cat_linear_speed, cat_angle, mouse_angle, mouse, arena, stoptime, fill=orange, **style):
        Turtle.__init__(self, position, heading, fill=fill, **style)
        # heading is the angle of the turtle's direction
        self.radius = radius
        self.cat_radius = cat_radius
        self.cat_cycle_speed = cat_cycle_speed
        self.cat_linear_speed = cat_linear_speed
        self.cat_angle = cat_angle
        self.mouse_angle = mouse_angle
        # print(mouse_angle)
        self.heading = self.cat_angle - 90
        #self.position = self.position + unit(self.heading + 90)*self.radius
        self.position = self.position + unit(self.heading + 90)*self.cat_radius
        self.mouse = mouse
        self.arena = arena
        self.stoptime = stoptime

    def getnextstate(self):
        self.arena.radius_label.config(text = 'CatRadius [m]: ' + str(round(self.cat_radius/100,3)))
        self.arena.angle_label.config(text = 'CatAngle [°]: ' + str(round((self.heading + 90)%360,3)))
        if int(self.arena.get_timestamp()) > int(self.stoptime):
            print('Ugh, I give up.')
            self.arena.stop()
            return self.position, self.heading
        else:
            self.cat_radius = ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5
            self.cat_angle = self.heading + 90
            if ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5 <= self.radius:
                C = self.heading - 360/(2*math.pi*self.radius/self.cat_cycle_speed)
                A = self.heading
                B = self.mouse.heading
                if math.cos((B-A)*math.pi/180) > math.cos((C-A)*math.pi/180) and math.cos((C-B)*math.pi/180) > math.cos((C-A)*math.pi/180):
                    # when the cat radius is 1.0 and the mouse angle lies between the old cat angle and the new cat angle.
                    # An angle B is between angles A and C in the following circumstances:
                    # cos (B - A) > cos (C - A), and cos (C - B) > cos (C - A) (angles in radian)
                    # The difference C - A is assumed to be less than 90°, or π/2 radians.
                    print('I got you at ' + str(self.arena.get_timestamp()/10**3) + ' seconds!')
                    # get_timestamp returns current simulation time (in milliseconds)
                    self.arena.stop()
                    return self.position, self.heading
                else:
                    print('I am coming!')
                    self.heading = self.heading - 360/(2*math.pi*self.radius/self.cat_cycle_speed)
                    self.position = self.position + unit(self.heading)*self.cat_cycle_speed
                    return self.position, self.heading
            elif ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5 > self.radius and (self.cat_radius) * math.cos((self.cat_angle - (self.mouse.heading + 90))*math.pi/180) >= 1.0:
                print('I am coming!')
                self.heading = self.heading
                self.position = self.position + unit(self.heading - 90)*self.cat_linear_speed

                return self.position, self.heading
            elif ((self.position.x-200)**2 + (self.position.y-200)**2)**0.5 > self.radius and (self.cat_radius) * math.cos((self.cat_angle - (self.mouse.heading + 90))*math.pi/180) < 1.0:
                print('Where is the mouse? I am circling.')
                self.heading = self.heading - 360/(2*math.pi*self.cat_radius/self.cat_cycle_speed)
                self.position = self.position + unit(self.heading)*self.cat_cycle_speed
                return self.position, self.heading
