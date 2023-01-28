import numpy as np

mm_to_cm = 1e-1
mass_leadbrick = 11.34*3*25*10/1000 #kg

def getThickness(density, length):
    '''
    Calculates the thickness of a material with a certain density in g/cm². The initial thickness 'length' is given in mm.
    '''
    return density*length*mm_to_cm

def getRelativeAttenuation(coefficient, thickness):
    '''
    Calculates the energy dependent attenuation of photons while passing a material. The material has a mass attenuation coefficient 'coefficient', given in cm²/g. The material thickness has to be given in g/cm². 
    '''
    return np.exp(-coefficient*thickness) 
