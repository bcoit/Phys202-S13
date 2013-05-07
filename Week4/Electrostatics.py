def pointField(x,y,q,Xq,Yq):
    """Takes the arrays (x,y), charge q, and position (Xq,Yq) as arguments and returns a tuple of electric field components (Ex,Ey)"""
    k=8.987551787e9 #units of k: N*m^2/C^2
    Ex = k*q*(x-Xq)/(((x-Xq)**2+(y-Yq)**2)**(1/2.))
    Ey = k*q*(y-Yq)/(((x-Xq)**2+(y-Yq)**2)**(1/2.))
    ExEy = [Ex, Ey]
    return ExEy

def pointPotential(x,y,q,posx,posy):
    """This function will take an x-y coord, charge, and position of the charge and return the potential at that x-y point"""
    k=8.987551787e9 #units of k: N*m^2/C^2
    Vxy = (k*q/((x-posx)**2+(y-posy)**2)**(1/2.))
    return Vxy

def dipolePotential(x,y,q,d):
    """This function will determine the potential at x,y due to a dipole, instead of a single point charge"""
    Vxy = pointPotential(x,y,q,-d,0.) - pointPotential(x,y,q,d,0.)
    return Vxy


