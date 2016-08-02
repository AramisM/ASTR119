import numpy as np

class Rock:
	def __init__(self, x, y, vx, vy, m, dens):
		self.x_pos = x
		self.y_pos = y
		self.x_vel = vx
		self.y_vel = vy
		self.mass = m
		self.density = dens
		self.radius = ((3.*mass)/(4. * np.pi * density))**(1/3)
		#self.traj = np.array([x_pos,y_pos,x_vel,y_vel,mass])