def pointPotential(x,y,q,posx,posy):
    """This function will take an x-y coord, charge, and position of the charge and return the potential at that x-y point"""
    k=8.987551787e9 #units of k: N*m^2/C^2
    Vxy = (k*q/((x-posx)**2+(y-posy)**2)**(1/2.))
    return Vxy

def dipolePotential(x,y,q,d):
    """This function will determine the potential at x,y due to a dipole, instead of a single point charge"""
    Vxy = pointPotential(x,y,q,-d,0.) - pointPotential(x,y,q,d,0.)
    return Vxy


