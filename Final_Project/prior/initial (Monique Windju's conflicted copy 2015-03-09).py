# import necessary function definitions
import numpy as np
import numpy.random as rnd
import scipy.constants as sc

dens = 2.65e6 # grams per cubic centimeter for granite

# class definition

class Rock:
	def __init__(self, x, y, vx, vy, m):#, dens):
		self.x_pos = x
		self.y_pos = y
		self.x_vel = vx
		self.y_vel = vy
		self.mass = m
		self.density = dens
		self.radius = ((3.*m)/(4. * np.pi * dens))**(1./3.)
		self.traj = np.array([x,y,vx,vy,m])

def grandom(mu,N):
    # Mean ("center") of the distribution, Std, Output shape
    noise = np.random.normal(loc=mu, scale=np.sqrt(mu), size=N)
    return noise

def initial(N=1000,moon_mass=7.35e22,moon_dist=384400000.,M=5.972e24):

	mu = moon_mass/N # average mass of an object
	
	# generate random parameters
	rand_mass = grandom(mu,N)
	rand_a = grandom(moon_dist,N)
	rand_e = rnd.rand(N)

	# convert input arrays to float64 type
	a = np.float64(rand_a)
	e = np.float64(rand_e)
	m = np.float64(rand_mass)
	
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


	