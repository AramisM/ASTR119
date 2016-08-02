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
def gen_plot(rock_list, Earth, moon_dist, max_mass, max_index, dist_scale, window = 1, orb_step = 0, unit_conv = (1.,'m'),p_scale = 1.,r_scale = 1.,n_col=0.0,frac_comp = 0.0):
	
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
	earthCircle = plt.Circle((Earth.x_pos, Earth.y_pos), radius = Earth.radius *p_scale, color = 'g', label='Earth')
	fig.gca().add_artist(earthCircle)
	
	# plot each rock
	rockCircle_l = plt.Circle((rock_list[max_index].x_pos, rock_list[max_index].y_pos), radius = rock_list[max_index].radius*30., color = 'r', label='Largest Rock')
	for i in rock_list:
		if i != max_index:
			rockCircle = plt.Circle((i.x_pos, i.y_pos), radius = i.radius*r_scale, color = 'k')
			fig.gca().add_artist(rockCircle)
	    		
	# add a title to the plot
	ax.set_title('Moon Formation Simulation')

	l = 0.02
	h = 0.16
	
	# add text
	ax.text(l, h, 'Elapsed Time: {:6.4f} months'.format(orb_step*3.805e-7), 
			verticalalignment='center',
			transform=ax.transAxes)
			
	# add text
	ax.text(l, h-0.03, 'Simulation Progress: {:6.4f}%'.format(frac_comp), 
			verticalalignment='center',
			transform=ax.transAxes)
			
	# add text
	ax.text(l, h-0.06, 'Number of Rocks: {}'.format(len(rock_list)), 
			verticalalignment='center',
			transform=ax.transAxes)
			
	# add text
	ax.text(l, h-0.09, 'Largest Rock: {:6.2e} kg'.format(max_mass), 
			verticalalignment='center',
			transform=ax.transAxes)
			
	# add text
	ax.text(l, h-0.12, 'Collisions: {}'.format(n_col), 
			verticalalignment='center',
			transform=ax.transAxes)
			
	plt.legend([rockCircle_l,earthCircle], ['Largest Rock','Earth'],loc='lower right')
		
	plt.draw()
		
	# return nothing
	return None