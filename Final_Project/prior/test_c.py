import numpy as np
import scipy.constants as sc
import scipy.integrate as integ
from scipy import spatial as sp

class Rock:
    def __init__(self, x, y, vx, vy, m):
        self.x_pos = x
        self.y_pos = y
        self.x_vel = vx
        self.y_vel = vy
        self.mass = m
        self.traj = np.array([self.x_pos,self.y_pos,self.x_vel,self.y_vel,self.mass])
        
def derivs(Rock_array, t, M_earth):
    
    # Distance between the center of the Earth and the moving body.
    r = np.sqrt((Rock_array[0])**2 + (Rock_array[1])**2)
        
    # Defines derivatives to be used in advOdeInt.
    
    dx1dt = Rock_array[2]
    dy1dt = Rock_array[3]
    dvx1dt = sc.G*M_earth*(Rock_array[0])/(r**2)
    dvy1dt = sc.G*M_earth*(Rock_array[1])/(r**2)
    
    return np.array([dx1dt, dy1dt, dvx1dt, dvy1dt])
    
    
def advOdeInt(rock, tstep, M_earth):
    # Makes a set of times to pass to odeint function, containing 0 and tstep.
    t_set = np.array([0,tstep])
    
    # Saves the attributes necessary for odeint as an array of initial conditions.
    Rock_array = np.array([rock.x_pos, rock.y_pos, rock.x_vel, rock.y_vel])
    
    #print Rock_array
    
    # Returns the most recent array of updated values.
    new_Rock = integ.odeint(derivs, Rock_array, t_set, args = (M_earth,))[1]
    
    # Takes the new values and updates the objects attributes.
    rock.x_pos = new_Rock[0]
    rock.y_pos = new_Rock[1]
    rock.x_vel = new_Rock[2]
    rock.y_vel = new_Rock[3]
    
    #print new_Rock
    
def collision_detection(rock_list):
    rock_pos_list = []
    for i in range(0, len(rock_list)):
        rock_pos_list.append((rock_list[i].x_pos, rock_list[i].y_pos))
    #print rock_pos_list
    tree = sp.KDTree(rock_pos_list)
    #nearest1 = tree.query_ball_tree(tree, r=4)
    #nearest2 = tree.query_ball_point((5,0), 4)
    nearest3 = tree.query_pairs(8)
    #print nearest1
    #print nearest2
    #print nearest3
    return None

def collision_result(rock1, rock2):
    # calculates mass and velocity components of new Rock object
    newMass = (rock1.mass + rock2.mass)
    pix = rock1.x_vel * rock1.mass + rock2.x_vel * rock2.mass
    piy = rock1.y_vel * rock1.mass + rock2.y_vel * rock2.mass
    newVx = pix / (newMass)
    newVy = piy / (newMass)
    
    # calculates center of mass to find x and y coordinates of new Rock object
    newX = (rock1.mass * rock1.x_pos + rock2.mass * rock2.x_pos) / newMass
    newY = (rock1.mass * rock1.y_pos + rock2.mass * rock2.y_pos) / newMass
    
    # creates and returns the new Rock object created by the collision.
    return Rock(newX, newY, newVx, newVy, newMass)
    
    
def tester(tstep = 1.e-3, tmax = .01):
    rock1 = Rock(1.e5, 1.e6, 1985.63, 19856.263, 1.e3)
    rock2 = Rock(1.e6, 1.e5, 19856.263, 1985.63, 1.e3)
    #rock3 = collision_result(rock1, rock2)
    #print rock3.traj
    rock_list = [rock1, rock2]
    M_earth = 6.e24
    
    for j in np.arange(0, tmax + tstep, tstep):        
                    
        for i in np.arange(len(rock_list)):
            #print 'For ' + str(i + 1) + 'th Rock:'
            advOdeInt(rock_list[i], tstep, M_earth)
    
        collision_detection(rock_list)