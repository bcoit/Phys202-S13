import numpy as np
import initialCond as ic
import CA184andSTCA as mod
import ASEP
def mult_time_steps(N,method,L,cars,v_max,p):
    """Given a method, number of time steps N, road length L, number of cars, and
probability p, this functions returns the density,and the positions of the cars,
 the average velocity and the average current for each time step"""
    road, x, v = ic.create_road(L, cars, v_max)
    pos = np.zeros((N, len(x)), int)
    vel = np.zeros
    current = np.zeros(N)
    density = cars/float(L)
    v_avg = np.zeros(N)
    if method == 'CA184':
        for i in range(N):
            x, v = mod.CA184(x,v,road,v_max)
            pos[i] = x
            v_avg[i] = average(v)
            current[i] = density * v_avg[i]
    if method == 'STCA':
        for i in range(N):
            x, v = mod.STCA(x,v,road,v_max,p)
            pos[i] = x
            v_avg[i] = average(v)
            current[i] = density * v_avg[i]
    if method == 'ASEP':
        for i in range(N):
            x, v = ASEP.ASEP(x,v,road,v_max)
            pos[i] = x
            v_avg[i] = average(v)
            current[i] = density * v_avg[i]
    return density, pos, v_avg, current
