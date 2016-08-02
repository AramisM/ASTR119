# the main file that controls the simulation
# Written by the group

# import function and class definitions
import initial
import AraLuc_Trynewthings as check
import plot_c
import numpy as np
import adv
import overlap_check as oc
from rock import Rock

# main function definition that runs the simulation
# arguments:
#	N: number of rocks to generate (1000 by default)
#	moon_mass: total mass of the rocks to generate (default to moon mass)
#	moon_dist: mean distance from planet to satellite (default to Earth-Moon distance)
#	M: mass of planet (default to Earth mass)
#	tstep: timestep of the simulation
#	tmax: duration of the simulation
#	plot_int: plot interval (in terms of time steps)
def main(N=1000,moon_mass=7.35e22,moon_dist=384400000.,M=5.972e24, tstep=1.0e2, tmax=1.0e5, plot_int = 1000):

	# generate initial conditions (planet and list of rocks)
	planet, rock_list, x = initial.initial(N,moon_mass,moon_dist,M)
	
	# check for (and remove) any overlaps of rocks with the planet from initial conditions
	rock_list = oc.out_check(planet, rock_list)
	
	# check for and handle any collisions in the rocks from initial conditions
	rock_list, collision_count_init, y = check.c_finder(rock_list)
	
	# plot the initial conditions
	plot_c.gen_plot(rock_list,planet,moon_dist)

	'''# create a counter for total collisions and loop through time steps
	tot_col_cnt = 0
	for j in np.arange(0 , tstep + tmax, tstep):
		
		# advance the rocks by one step
		rock_list = adv.advOdeInt(rock_list, tstep, planet)
		
		# advance the planet by one step
		planet = adv.newPlanet(rock_list, planet)
		
		# check and handle any overlaps of the rocks and planet
		rock_list = oc.out_check(planet, rock_list)
		
		# check for and handle collisions
		rock_list, collision_count = check.c_finder(rock_list)
		
		# increment the total collision counter if a collision(s) occur
		tot_col_cnt += collision_count
		
		print 'Total Collisions: {}'.format(tot_col_cnt)
	    
		# if the appropriate time step, then plot the system
		if j % plot_int == 0:
			plot_c.gen_plot(rock_list,planet,0.1* moon_dist,orb_step=j,scale=1.)
	'''
	