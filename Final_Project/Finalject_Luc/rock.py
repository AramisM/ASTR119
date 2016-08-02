import numpy as np
dens=2.65e3

class Rock:
	def __init__(self, x, y, vx, vy, m):
		self.x_pos = x
		self.y_pos = y
		self.x_vel = vx
		self.y_vel = vy
		self.mass = m
		#self.density = dens
		self.radius = ((3.*m)/(4. * np.pi * dens))**(1./3.)