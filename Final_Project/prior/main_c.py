#from Rock import Rock
#from dir import Dir
import initial
import AraLuc_Trynewthings as check
import plot_c
import numpy as np
import adv

dens=2.65e6

class Rock:
	def __init__(self, x, y, vx, vy, m):
		self.x_pos = x
		self.y_pos = y
		self.x_vel = vx
		self.y_vel = vy
		self.mass = m
		#self.density = dens
		self.radius = ((3.*m)/(4. * np.pi * dens))**(1./3.)

# main function

def main(N=1000,moon_mass=7.35e22,moon_dist=384400000.,M=5.972e24):

	planet, rock_list = initial.initial(N,moon_mass,moon_dist,M)
	
	#rock_list = check.c_finder(rock_list)
	
	plot_c.gen_plot(rock_list,planet,moon_dist)
	
	tstep = 1.0e-3
        tmax = 0.001
	
	for j in np.arange(0 , tstep + tmax, tmax):
	    
	    adv.advOdeInt(rock_list, tstep, planet)
	    adv.newPlanet(rock_list, planet)
	    #plot_c.gen_plot(rock_list,planet,moon_dist)
	    