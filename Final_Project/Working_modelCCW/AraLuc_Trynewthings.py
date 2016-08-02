import numpy as np
from scipy import spatial as sp
from rock import Rock

dens = 2.65e3
def get_distance(rock1,rock2):
    distance = np.sqrt((rock1.x_pos - rock2.x_pos)**2+(rock1.y_pos - rock2.y_pos)**2)
    return distance  

def collision_prelim(rock_list,max_radius):
    rock_pos_list = []
    for i in range(0, len(rock_list)):
        rock_pos_list.append((rock_list[i].x_pos, rock_list[i].y_pos))
    #print rock_pos_list
    tree = sp.KDTree(rock_pos_list)
    #Here you input the radius for which the binary tree will consider these to be near
    nearest_pairs = list(tree.query_pairs(max_radius*2))
    #print nearest_pairs
    if(len(nearest_pairs) > 0):
        nearest_pairs = sorted(nearest_pairs)
        #print 'near pairs:', nearest_pairs
    return nearest_pairs
  
def collision_check(nearest_pairs, rock_list):
    collision_pairs = []
    for i in nearest_pairs:
        d = get_distance(rock_list[i[0]],rock_list[i[1]]) # Distance between rocks.
        # If distance between the rocks centers is less than their combined radii,
        # Append the pair to a list called collision pairs and print a celebratory message!
        if d < (rock_list[i[0]].radius + rock_list[i[1]].radius):
            collision_pairs.append([i[0], i[1]])
            print "We got a collision! "
            print "masses of ",  rock_list[i[0]].mass, "and", rock_list[i[1]].mass
            print "positions of ", "(", rock_list[i[0]].x_pos, rock_list[i[0]].y_pos, ")", "(", rock_list[i[1]].x_pos, rock_list[i[1]].y_pos, ")"
    if (len(collision_pairs) > 0):
        print "We had collisions: "
        print collision_pairs
    return collision_pairs
    
#****************************************************************************************************
# Takes in collision_pairs and makes new "sets" that takes into account intersections,
# AKA multibody collisions.
# i.e. [(1,2),(1,7),(5,6),(7,8),(9,10)] becomes [[1,2,7,8],[5,6],[9,10]]

def multicollision_catcher(collision_pairs):
    collision_counter = 0
    multi_collision_list = []
    multi_collision_list.append([collision_pairs[0][0], collision_pairs[0][1]])
    for t in range(1, len(collision_pairs)):
        multi = False
        for i in range(0,len(multi_collision_list)):
            if collision_pairs[t][0] in multi_collision_list[i]:
                multi_collision_list[i].append(collision_pairs[t][1])
                multi = True
            elif (collision_pairs[t][1] in multi_collision_list[i]):
                multi_collision_list[i].append(collision_pairs[t][0])
                multi = True
        if(multi == False):
            multi_collision_list.append([collision_pairs[t][0],collision_pairs[t][1]])
    #print multi_collision_list
    #Removes any repetitions from multi_collision_list
    for c in range(0,len(multi_collision_list)):
        multi_collision_list[c] = list(set(multi_collision_list[c]))
    #print multi_collision_list
    collision_counter = len(multi_collision_list)
    return multi_collision_list, collision_counter

def multicollision_result(multi_collision_list, rock_list):
    for a in range(0, len(multi_collision_list)):
        if len(multi_collision_list[a]) == 2:
            newRock = collision_result(rock_list[multi_collision_list[a][0]],rock_list[multi_collision_list[a][1]])
            rock_list.append(newRock)
            rock_list[multi_collision_list[a][0]].mass = 0 #Sets m of rock gone to 0 (can be done later)
            rock_list[multi_collision_list[a][1]].mass = 0 #Sets m of rock gone to 0 
        else:
            newRock = collision_result(rock_list[multi_collision_list[a][0]],rock_list[multi_collision_list[a][1]])
            rock_list[multi_collision_list[a][0]].mass = 0 #Sets m of rock collided to 0 (can be done later)
            rock_list[multi_collision_list[a][1]].mass = 0 #Sets m of rock collided to 0 
            for c in range(2, len(multi_collision_list[a])):
                newRock = collision_result(newRock,rock_list[multi_collision_list[a][c]])
                rock_list[multi_collision_list[a][c]].mass = 0 # Sets m of rock collided to 0
            #Appends big rock, resulting from multiple collisions to the rock_list 
            rock_list.append(newRock)
    return rock_list

#****************************************************************************************************

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


def c_finder(rock_list):
    #rock0 = Rock(0., 0., 0., 0., 0.)
    #rock1 = Rock(1., 2., 5., 3., 8.)
    #rock2 = Rock(6., 1., 4., 3., 11.)
    #rock3 = collision_result(rock1, rock2)
    #print rock3.traj
    #rock_list = [rock0, rock1, rock2]
    #print rock_list
    #new_rock_list = rock_list
    # Find the max_radius of rock_list
    #mass_array = np.array(rock_list[0:-1].mass)
    #np.maximum(mass_array)
    
    max_radius = 0
    for b in range(0, len(rock_list)):
        if (rock_list[b].radius > max_radius):
            max_radius = rock_list[b].radius
            index_biggest = b
    #print max_radius
    collision_pairs = collision_check(collision_prelim(rock_list,max_radius), rock_list)
    collision_count = 0
    if (len(collision_pairs) != 0):
        multi_pairs, collision_count = multicollision_catcher(collision_pairs)
        rock_list = multicollision_result(multi_pairs, rock_list)
        #print "here it comes"
        # Removes objects with mass 0 (objects that have collided) from list
        # Get new max_radius
        size = len(rock_list) -1
        for c in range(0, len(rock_list)):
            if (rock_list[size-c].mass == 0):
                rock_list.remove(rock_list[size-c])
            elif(rock_list[size-c].radius > max_radius):
                max_radius = rock_list[size-c].radius
        #print "here comes the masses of the list"
        for b in range(0, len(rock_list)):
            if(rock_list[b].radius == max_radius):
                index_biggest = b

    return rock_list, collision_count, max_radius, (4*np.pi*dens*(max_radius**3)/3), index_biggest
        
    
    #multicollision_catcher([(1,2),(1,3),(1,4),(1,9),(3,4),(5,10),(6,10),(10,12)])
    #print get_Radius(rock1)
    #print get_Radius(rock2)
    