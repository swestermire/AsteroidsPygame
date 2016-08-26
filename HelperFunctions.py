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

def pting_vector_angle(pting_vector):
    if pting_vector[0] < 0.00001:
        pting_vector[0] = .00001
    elif pting_vector[1] < 0.0001:
        pting_vector[1] = .0001
        
    angle = math.degrees(math.atan(float(pting_vector[1])/float(pting_vector[0])))
    return angle
    
