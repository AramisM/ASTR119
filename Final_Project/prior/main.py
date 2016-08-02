# the main file that controls the simulation
# Written by the group

# import function and class definitions
import initial
import AraLuc_Trynewthings as check
import plot_c
import numpy as np
import adv
import overlap_check as oc
import math
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
def main(N=500,moon_mass=4*7.35e22,moon_dist=0.5*384400000.,M=5.972e24, tstep=0, tmax=1.0e6, plot_int = 100.):

	# generate initial conditions (planet and list of rocks)
	planet, rock_list, P_min = initial.initial(N,moon_mass,moon_dist,M)
	
	# check for (and remove) any overlaps of rocks with the planet from initial conditions
	rock_list = oc.out_check(planet, rock_list)
	
	# check for and handle any collisions in the rocks from initial conditions
	rock_list, collision_count_init, indices_of_colli_rocks = check.c_finder(rock_list)
	
	# plot the initial conditions
	plot_c.gen_plot(rock_list,planet,moon_dist,n_col=collision_count_init)
	
	# if tstep is not specified by the user, set it to 1000th of the smallest period from
	#	initial conditions and round up
	if tstep == 0:
		tstep = P_min/10000.
		
	print 'Commencing the simulation...'
	print '    Initial Time Step: {}'.format(tstep)

	# create a counter for total collisions and loop through time steps
	tot_col_cnt = 0
	ctr = 0
	for j in np.arange(0 , tstep + tmax, tstep):

		# advance the rocks by one step
		rock_list = adv.advOdeInt(rock_list, tstep, planet)
		
		# check and handle any overlaps of the rocks and planet
		rock_list = oc.out_check(planet, rock_list)
		
		# check for and handle collisions
		rock_list, collision_count, indices_of_colli_rocks = check.c_finder(rock_list)
		
		# increment the total collision counter if a collision(s) occur
		tot_col_cnt += collision_count
	    
		# if the appropriate time step, then plot the system
		if ctr % plot_int == 0:
			plot_c.gen_plot(rock_list,planet,moon_dist,orb_step=j,n_col=tot_col_cnt+collision_count_init)
		
		ctr += 1
		
		print tot_col_cnt
		print ctr
	
	