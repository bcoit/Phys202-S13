 
def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying
data and perform a linear least squares regression.  Return the resulting slope
and intercept parameters of the best fit line with their uncertainties."""
    x_avg = sum(x)/len(x)
    y_avg = sum(y)/len(y)
    xx_avg = sum(x**2)/len(x)
    xy_avg = sum(x*y)/len(x)
    slope = (xy_avg - x_avg*y_avg)/(xx_avg - x_avg**2)
    intercept = (xx_avg*y_avg - x_avg*xy_avg)/(xx_avg - x_avg**2)
    err_avg = sum((y-slope*x-intercept)**2)/len(x)
    slerr = (err_avg/((len(x)-2)*(xx_avg-x_avg**2)))**(.5)
    interr = ((err_avg*xx_avg)/((len(x)-2)*(xx_avg-x_avg**2)))**(.5)
    return slope, intercept, slerr, interr


def WeightedLinearLeastSquaresFit(x,y,weight):
    """Take in arrays representing (x,y) values for a set of linearly varying
data and an array of weights w.  Perform a weighted linear least squares
regression.  Return the resulting slope and intercept parameters of the best
fit line with their uncertainties.
If the weights are all equal to one, the uncertainties on the parameters are 
calculated using the non-weighted least squares equations."""
    w = sum(weight)
    weightless = True
    for i in weight:
        if i != 1:
            weightless = False
    if weightless:
        return LinearLeastSquaresFit(x,y)

    wx = sum(weight*x)
    wxx = sum(weight*x**2)
    wy = sum(weight*y)
    wxy = sum(weight*x*y)

    intercept = (wxx*wy-wx*wxy)/(w*wxx-wx**2)
    slope = (w*wxy-wx*wy)/(w*wxx-wx**2)
    slerr = (w/(w*wxx-wx**2))**.5
    interr = (wxx/(w*wxx-wx**2))**.5

    return slope, intercept, slerr, interr

