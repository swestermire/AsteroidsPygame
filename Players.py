import Physics as physicsFile

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
        
        
        
        
        
        
        
    '''
    def thrust_on_off(self, state):
        if state == 'on':
            self._thrust_state = True
        elif state == 'off':
            self._thrust_state = False
        elif state == True or state == False:
            self._thrust_state = state
        else:
            print('Thrust input error, look at def thrust_on_off function')
            
    def get_vel(self):
        return self._linear_vel
        
    def set_pos(self):
        self._pos[0] += self._linear_vel[0]
        self._pos[1] += self._linear_vel[1]

    def reset_pos(self, screen_height, screen_width):
        self._pos = [screen_width/2, screen_height/2]
        
    def get_pos(self):
        self.vel_acc(self._pointing_vector)
        return self._pos

    def update_pting_vector(self, angle):
        self._pointing_vector = angle #need to update    

    def vel_acc(self, pting_vector):
        if self._thrust_state:
            if HF.calc_speed(self._linear_vel) < self._max_linear_vel:
                self._linear_vel[0] += pting_vector[0] * self._linear_acc[0]
                self._linear_vel[1] += pting_vector[1] * self._linear_acc[1]
            elif HF.calc_speed(self._linear_vel) > self._max_linear_vel:
                # need to adjust velocity if velocity is over max
                None

        self.set_pos()
    '''

    
        
