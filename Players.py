import Physics as physicsFile
import random

class Player(physicsFile.Physics):
    '''
    Player class will control all the players stats, score, etc.
    '''

    def __init__(self):
        self._player_lives = 3
        self._linear_acc = [0.1,0.1]
        self._angular_vel = 0.1
        self._max_linear_vel = 2
        self._linear_vel = [0,0]
        self._pointing_vector = [1,0]

        self._thrust_state = False
        self._rotation_state = False
        
        self._player_state = {"max velocity" : 5 ,
                              "angular velocity" : 1 ,
                              "pointing vector" : [1,0],
                              "ship angle" : 0,
                              "rotation state" : False , 
                              "thrust state" : False,
                              'draw handler obj' : ""}
                              
class Asteroids(physicsFile.Physics):
    '''
    class for asteroids that spawn in-game
    '''
    def __init__(self):
        self._state = { "active asteroids hash" : {},
                        "asteroid count" : 0,
                        "asteroid spawn counter" : 0,
                        "asteroid spawn frequency" : 120}
                        
    def spawnAsteroid(self):
        '''
        Spawn asteroids based on number of times this function is called.  This basically
        works as a rough counter.
        '''
        self._state["asteroid spawn counter"] += 1
        
        if (self._state["asteroid spawn counter"] % self._state["asteroid spawn frequency"] == 0):
            self.addAsteroid()
            self._state["asteroid spawn counter"] = 0
            
    def addAsteroid(self):
        randomVal = random.randint(0,100)/100
        
        asteroidDict = {"velocity": [random.randint(0,5),
                                     random.randint(0,5)] ,
                        "pointing vector" : [randomVal, 1-randomVal],
                        "angle" : 0,
                        "rotation state" : True,
                        "thrust state" : True,
                        "angular velocity" : random.randint(1,150)/100,
                        "asteroid state" : "active",
                        "position" : [random.randint(0,700),
                                      random.randint(0,700)] }
         
        self._state["active asteroids hash"][self._state["asteroid count"]] = asteroidDict
        self._state["asteroid count"] += 1
    
    def updateAsteroidPositions(self, canvasDrawStates):
        '''
        Updates all asteroid positions based on their velocity and point vector
        '''
        for asteroid in self._state["active asteroids hash"].values():
            position = asteroid["position"]
            position[0] += asteroid["pointing vector"][0] * asteroid['velocity'][0]
            position[1] += asteroid["pointing vector"][1] * asteroid['velocity'][1]
            
            xPos, yPos = self.asteroidsBoundaryCheck(position[0], 
                                                     position[1],
                                                     canvasDrawStates)            
            asteroid["position"] = [xPos, yPos]
            

    def hitAsteroid(self, asteroidID):
        '''
        behaviors that take place when an asteroid is hit
        '''        
        self._state["active asteroids hash"][asteroidID]["asteroid state"] = "exploding"        
        
        
    def destroyAsteroid(self, asteroidID):
        '''
        destroys asteroid from self._asteroids_state based on passed index val
        '''
        
        # Was thinking about making an inactive status for asteroids, but this would
        # bog down on image rendering
        # self._state["active asteroids hash"][asteroidID]["asteroid state"] = "destroyed"
        
        del self._state["active asteroids ID"][asteroidID]
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
