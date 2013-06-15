import numpy as np

def g_for_STCA(x, v, road):
    """Takes x, v, and road arrays as arguments and calculated the spacing 
between each car.  The output is a gi array to be used in the STCA and CA184
models so that all cars can be moved in one time step instead of one at a 
time."""
    L = len(road)
    b = 0
    sortedx = sorted(x)
    gi = np.zeros(x.shape, int)
    for i in range(0, len(x)):
        a = x[i]
        for j in range(0, len(x)):
            if sortedx[j] == a:
                if j <= len(sortedx)-2: #calculating g for all but the last car
                    b = sortedx[j+1]
                    gi[i] = b - a - 1
                else:
                    gi[i] = L + sortedx[0] - sortedx[-1] - 1 #calculating g for the last car on the road
    return gi

def CA184(x, v, road, v_max):
    """takes an array of car positions and initial velocities, a road length, 
and a maximum velocity as arguments.  Returns the final positions and velocities
of the cars after one time step by moving all the cars at once, following the
CA184 model.  In this model there is no possibility of random slow-downs"""
    gi = g_for_STCA(x, v, road)
    L = len(road)
    for i in range(0, len(v)):
        if gi[i] == 0:
            v[i] = 0
        elif v[i] >= gi[i]:
            v[i] = gi[i]
        elif v[i] < gi[i] and v[i] < v_max:
            v[i] += 1
        x[i] += v[i]
        if x[i] > L:
            x[i] = x[i] - L
    return x, v

def STCA(x, v, road, v_max, p):
    """Takes an array of car positions and initial velocities, a road lenght, a
maximum velocity and a random slow-down probability p as arguments.  p must be a
value between 1 and 100.  The final position and velocities of the cars are 
returned after one time step.  The cars are all moved at once, and the possibility
of random slow-downs is allowed, following the STCA model of traffic flow"""
    gi = g_for_STCA(x, v, road)
    L = len(road)
    for i in range(0, len(v)):
        if gi[i] == 0:
            v[i] = 0
        elif v[i] >= gi[i]:
            v[i] = gi[i]
        elif v[i] < gi[i] and v[i] < v_max:
            v[i] += 1
        if v[i] > 0: #Allowing the possibility for random slowdowns
            if np.random.random_sample < (1/100.)*p:
                v[i] -= 1
        x[i] += v[i]
        if x[i] > L:
            x[i] = x[i] - L
    return x, v

