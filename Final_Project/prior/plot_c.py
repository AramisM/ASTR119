# Plotting functions for the orbital system
# Written by Cesar Gonzalez Renteria and Benjamin Stahl

# import necessary functions and class definitions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rock import Rock # rock class definition


# define plotting function: gen_plot
# will plot the positions of the rocks and planet
# Mandatory arguments
#	rock_list: the list of rocks
#	Earth: The instance for Earth
#       density: The density of the rocks
# Optional arguments:
#	window: specifies figure window (def: 1)
#	orb_step: orbital time step that the simulation is on
#	unit_scale: multiplier to convert from meters to another unit (def: 1)
#	unit_name: unit scaled to (def: 'm')
def gen_plot(rock_list, Earth, moon_dist, window = 1, orb_step = 0, unit_conv = (1.,'m'), dist_scale=1.,p_scale = 1.,r_scale = 1.,n_col=0.0):
	
	# open/move to specified figure window
	fig = plt.figure(window,figsize=(8,8))
	
	# clear the figure in case there is anything left from before
	fig.clf()
	
	# create two subplots 
	ax = fig.add_subplot(111,adjustable='box', aspect=1.0)
 
	# set x and y limits of the subplot to a multiple of moon_dist
	ax.set_xlim([-dist_scale*unit_conv[0]*moon_dist,dist_scale*unit_conv[0]*moon_dist])
	ax.set_ylim([-dist_scale*unit_conv[0]*moon_dist,dist_scale*unit_conv[0]*moon_dist])
	
	# label axes
	ax.set_xlabel(r'$x$ Position ({})'.format(unit_conv[1]))
	ax.set_ylabel(r'$y$ Position  ({})'.format(unit_conv[1]))
	
	# plot Earth
	earthCircle = plt.Circle((Earth.x_pos, Earth.y_pos), radius = Earth.radius *p_scale, color = 'g')
	fig.gca().add_artist(earthCircle)
	
	# plot each rock
	for i in rock_list:
	    rockCircle = plt.Circle((i.x_pos, i.y_pos), radius = i.radius*r_scale, color = 'b')
	    fig.gca().add_artist(rockCircle)
	    
	#side_text = plt.figtext(0.6, 0.5, 'Time Step: {:6.2f}'.format(orb_step) + '\n' + 'Collisions: {:6.2f}'.format(n_col), bbox=dict(facecolor='white'))
		
	# add a title to the plot
	ax.set_title('Orbital Simulation')

	# add text
	ax.text(0.15, 0.15, 'Time Step: {:6.2f}'.format(orb_step) + '\n' + 'Collisions: {}'.format(n_col),
			horizontalalignment='center',
			verticalalignment='center',
			transform=ax.transAxes)
		
	plt.draw()
		
	# return nothing
	return None