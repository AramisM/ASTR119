import numpy as np
from scipy import spatial as sp
density = 3.2*10**3 #kg/m3
class Rock:
    def __init__(self, x, y, vx, vy, m):
        self.x_pos = x
        self.y_pos = y
        self.x_vel = vx
        self.y_vel = vy
        self.mass = m
        self.traj = np.array([self.x_pos,self.y_pos,self.x_vel,self.y_vel,self.mass])
        
def get_radius(rock):
    r = ((3*rock.mass)/(4*density*np.pi))**1/3 
    return r
    
def get_distance(rock1,rock2):
    distance = np.sqrt((rock1.x_pos - rock2.x_pos)**2+(rock1.y_pos - rock2.y_pos)**2)
    return distance
    

def collision_prelim(rock_list):
    rock_pos_list = []
    for i in range(0, len(rock_list)):
        rock_pos_list.append((rock_list[i].x_pos, rock_list[i].y_pos))
    print rock_pos_list
    tree = sp.KDTree(rock_pos_list)
    nearest_pairs = list(tree.query_pairs(8))
    print nearest_pairs
    return nearest_pairs
  
def collision_check(nearest_pairs, rock_list):
    collision_pairs = []
    for i in nearest_pairs:
        d = get_distance(rock_list[i[0]],rock_list[i[1]])
        if d < (get_radius(rock_list[i[0]]) + get_radius(rock_list[i[1]])):
            collision_pairs.append((i[0], i[1]))
            print "We got a collision"
    return collision_pairs
    
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

def tester():
    rock0 = Rock(0, 0, 0, 0, 0)
    rock1 = Rock(1, 2, 5, 3, 8)
    rock2 = Rock(6, 1, 4, 3, 11)
    #rock3 = collision_result(rock1, rock2)
    #print rock3.traj
    rock_list = [rock0, rock1, rock2]
    collision_check(collision_prelim(rock_list), rock_list)
    #print get_Radius(rock1)
    #print get_Radius(rock2)
    