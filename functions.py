import math

def bulk_density (pg, n, pw=997):
    """This function calculates the bulk density of a saturated material
    this function takes the arguments
     - density of grains (pg)
     - porosity of grains (n)
     - density of liquid (pw) #if not specified assumed water density 997 kg/m³
     to return the bulk density of a saturated porous material (pb)
     """
    pb = pg (1-n) + pw(n)
    return pb

def factor_of_safety (c, pb, h, theta,  wt, tan_phi, pw=997):
    """This function assesses the stability of a hill slope,
    by looking at the ratio of resisting stresses to driving stress
    this function takes arguments:
     - cohesion (c) #mineral or biological
     - bulk density of the material (pb),
     - height of hill slope (h)
     - angle of the hill slope (theta),
     - density of liquid (pw) #if not specified assumed water density 997 kg/m³
     - water table height above failure plane (wt)
     - internal angle of friction (tan_phi)
     - acceleration due to gravity at the Earth's surface is 9.8 (m/s²)
     and assesses the stability of the hill slope by finding Fs and seeing if it is greater or less than 1
     """
    fs= (c+(pb*9.87*h*(np.cos(theta)))-(pw*9.8*wt)*tan_phi)/(pb*9.87*h*np.sin(theta))
    if fs > 1:
        print("The factor of safety is", fs ,"therefore the slope should be stable")
    elif fs < 1:
        print("The factor of safety is", fs ,"the driving stress is exceeding the resistance and the slope is likely to fail")