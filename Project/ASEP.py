import numpy as np
def g_for_ASEP(x, v, i, road):
    """Takes x, v, and road arrays as well as a randomly generated integer, i, as
arguments.  This function determines the empty spaces in front of a randomly 
chosen car in order to be used in the ASEP traffic mode, returning a single g
value"""
    L = len(road)
    a = x[i]
    b = 0
    sortedx = sorted(x)
    for j in range(0, len(sortedx)):
        if sortedx[j] == a:
            if j <= len(sortedx)-2: #finding g for all but the last car
                b = sortedx[j+1]
                gi = b - a - 1
            else:
                gi = L + sortedx[0] - sortedx[-1] - 1 #calculating g for the last car on the road
    return gi

def ASEP(x, v, road, v_max):
    """Takes x, v, and road arrays as well as a maximum velocity as arguments.
The final positions and velocities of the cars are then returned after one time
step.  The cars are moved one at a time following the ASEP model of traffic flow"""
    L = len(road)
    n = range(len(x))
    i = 0
    np.random.shuffle(n)
    for j in range(len(n)):
        i = n[j]
        gi = g_for_ASEP(x, v, i, road)
        if gi == 0:
            v[i] = 0
        elif v[i] > gi:
            v[i] = gi
        elif v[i] < gi and v[i] < v_max:
            v[i] += 1
        x[i] += v[i]
        if x[i] > L:
            x[i] = x[i] - L
    return x, v

