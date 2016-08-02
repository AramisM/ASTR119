import numpy as np
import numpy.random as rnd
import scipy.constants as sc

# class definition

class Rock:
	def __init__(self, x, y, vx, vy, m):#, dens):
		self.x_pos = x
		self.y_pos = y
		self.x_vel = vx
		self.y_vel = vy
		self.mass = m
		#self.density = dens
		#self.radius = ((3.*mass)/(4. * np.pi * density))**(1/3)
		#self.traj = np.array([x_pos,y_pos,x_vel,y_vel,mass])

# Script written by Benjamin Stahl 03/05/15

# initial function
# mandatory arguments: (arrays need to be same shape)
#	a: a np array of semi-major axes
#	e: a np array of eccentricities 
#	M: mass of planet (Earth)
#	m: a np array of masses 

def initial(a,e,M,m):

	# convert input arrays to float64 type
	a = np.float64(a)
	e = np.float64(e)
	m = np.float64(m)
	
	# calculations are done using formulas from class 11
    # mass ratio 'q', total mass, initial distance, initial velocity
	
	q = np.float64(m/M)
	m_tot = np.float64(m + M)
	r_init = ((1. - e)/(1. + q)) * a
	v_init = (1./(1. + q)) * np.sqrt((1. + e)/(1. - e)) * np.sqrt(sc.G * m_tot/a)
	
	# generate N equally likely random angles between 0 and 2pi 
	
	ang = rnd.rand(len(a)) * 2 * np.pi
	
	# convention: x for particle 1 and X for particle 2
    # this is our array of initial values which will be 
    # calculated and stored within hw5()
	
	x = r_init * np.cos(ang)
	y = r_init * np.sin(ang)
	X = -q * r_init * np.cos(ang)
	Y = -q * r_init * np.sin(ang)
	vx = v_init * np.sin(ang)
	vy = v_init * np.cos(ang)
	vX = -q * v_init * np.sin(ang)
	vY = -q * v_init * np.cos(ang)
	
	# create a Rock instance for the Earth by taking the mean of all the Earth positions
	# and velocities
	
	Earth = Rock(np.mean(X),np.mean(Y),np.mean(vX),np.mean(vY),M)
	
	# create a Rock instances for each of the objects generated
	
	rocks = []

	for i in range(len(a)):
		rocks.append(Rock(x[i],y[i],vx[i],vy[i],m[i]))
	
	return Earth, rocks
	
