# Work in progress plot function for Final Project
# Cesar Gonzalez Renteria
# Nearly identical to Ben Stahl's gen_plot
import os
import numpy as np
import matplotlib.pyplot as plt
from rock import Rock
#from rock import Rock

'''
class Rock:
	def __init__(self, x, y, vx, vy, m):
		self.x_pos = x
		self.y_pos = y
		self.x_vel = vx
		self.y_vel = vy
		self.mass = m
		#self.density = dens
		self.radius = ((3.*m)/(4. * np.pi * dens))**(1./3.)'''

# define plotting function: gen_plot
# will plot the positions of the rocks and Earth
# Mandatory arguments
#	rock_list: the list of rocks
#	Earth: The instance for Earth
#       density: The density of the rocks
# Optional arguments:
#	window: specifies figure window (def: 1)
#	orb_step: orbital time step that the simulation is on
#	unit_scale: multiplier to convert from meters to another unit (def: 1)
#	unit_name: unit scaled to (def: 'm')

def gen_plot(rock_list, Earth, moon_dist, window = 1, orb_step = 0, unit_scale = 1, unit_name = 'm', scale=1.,filename='plot'):
	
	# open/move to specified figure window
	fig = plt.figure(window)
	
	# clear the figure in case there is anything left from before
	fig.clf()
	
	# create a subplot spanning the entire figure window
	ax = fig.add_subplot(111,adjustable='box', aspect=1.0)
	   
	# set x and y limits of the subplot to 2x the max radius of the rocks
	ax.set_xlim([-3.0*moon_dist*unit_scale,3.0*moon_dist*unit_scale])
	ax.set_ylim([-3.0*moon_dist*unit_scale,3.0*moon_dist*unit_scale])
	
	# label axes
	ax.set_xlabel(r'$x$ Position ({})'.format(unit_name))
	ax.set_ylabel(r'$y$ Position  ({})'.format(unit_name))
	
	'''# plot Earth
	ax.plot(Earth.x_pos*unit_scale, Earth.y_pos*unit_scale, 'go')
	
	# plot positions of rocks
	for i in rock_list:
	   ax.plot(i.x_pos*unit_scale, i.y_pos*unit_scale,'bo')
	
	'''
	
	# plot Earth
	earthCircle = plt.Circle((Earth.x_pos, Earth.y_pos), radius = Earth.radius *scale, color = 'g')
	fig.gca().add_artist(earthCircle)
	
	# Get the radius of each rock and plot them.
	for i in rock_list:
	    
	    rockCircle = plt.Circle((i.x_pos, i.y_pos), radius = i.radius*scale, color = 'r')
	    fig.gca().add_artist(rockCircle)
		
	# add a title to the plot that indicates the time step
	if orb_step == 0:
		ax.set_title('Orbital Simulation (Initial State)')
	else:
		ax.set_title('Orbital Simulation (Time Step: {})'.format(orb_step))
		
	h=1
	while os.path.exists('plot/{}{:d}.png'.format(filename, h)):
		h += 1
	plt.savefig('plot/{}{:d}.png'.format(filename, h),bbox_inches='tight')    
	#plt.savefig('plots/gen{j}.png').format(j=j)

	# return nothing
	return None
