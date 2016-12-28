'''
Helper functions for Asteroids Game
'''
import math

def calc_speed(val):
    speed = math.sqrt(val[0]**2 + val[1]**2)
    return speed

def rotate_vector(pting_vector, angle):
    rotated_vector = None
    return rotated_vector

def unit_vector(angle):
    # returns unit vectors x and y such that it represents the direction
    # of an entity
    # returns [x-unit vector, y-unit vector]

    radians = math.radians(angle)
    unitVector = [math.cos(radians), -1*math.sin(radians)]
    
    return unitVector

def pting_vector_angle(pting_vector):
    if pting_vector[0] < 0.00001:
        pting_vector[0] = .00001
    elif pting_vector[1] < 0.0001:
        pting_vector[1] = .0001
        
    angle = math.degrees(math.atan(float(pting_vector[1])/float(pting_vector[0])))
    return angle

def calcDistance(coord1, coord2):
    '''
    distance for 2 dimensional plane
    '''
    distance = math.sqrt(math.pow((coord1[0] - coord2[0]),2) + math.pow(coord1[1] - coord2[1],2))
    return distance
