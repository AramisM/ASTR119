import numpy as np
def out_check(planet, rock_list):
	rock_list = np.array(rock_list)
	t_arr = np.zeros(len(rock_list),dtype=bool)
	ctr = 0
	for i in rock_list:
		d = np.sqrt((i.x_pos - planet.x_pos)**2 + (i.y_pos - planet.y_pos)**2)
		if d > planet.radius:
			t_arr[ctr] = True
		ctr += 1
	return list(rock_list[t_arr])
		