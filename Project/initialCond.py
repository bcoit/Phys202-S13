import numpy as np
def create_road(L,cars,v_max):
    """Sets up the road, initial position, and initial velocity arrays to be
used as inputs for the traffic flow functions"""
    road = np.zeros(L, int)
    x = np.zeros(cars, int)
    v = np.zeros(cars, int)
    each_car = 1
    while (each_car <= cars):
        i = randint(0,L)
        if road[i] == 0: #check to make sure there isn't already a car in this position
        x[each_car-1] = i
        road[i] = each_car
        v[each_car-1] = randint(0,v_max) #assign each car a random velocity between 0 and the maximum velocity (speed limit)
        each_car += 1
    return road, x, v


