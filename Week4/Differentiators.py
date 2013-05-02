def finiteDifference(x,y):
    """Takes arrays x and y as inputs and returns the derivative of y with respect to x using a 2-point, centered method"""
    import numpy as np
    dydx = np.zeros(y.shape,float) #So we know dydx will be the same size as x and y
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def fourPtFiniteDiff(x,y):
    """This will take the derivative of a function y over a range x using a higher order, four-point, centered method"""
    import numpy as np
    dx = 0.1
    dydx = np.zeros(y.shape,float)
    for i in range(2,len(y)-2):
        dydx[i] = (y[i-2] - 8*y[i-1] + 8*y[i+1] - y[i+2])/(12*dx)
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    dydx[1] = (y[2] - y[1])/(x[2] - x[1])
    dydx[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])
    return dydx

