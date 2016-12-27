import HelperFunctions as HF

class Physics:
    '''
    Asteroids game physics
    '''

    def __init__(self):
        return
        
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
        '''
        calculates objects final position according to movement and screen boundary conditions
        '''
        xPos = self._pos[0] + self._linear_vel[0]
        yPos = self._pos[1] + self._linear_vel[1] 
        pos = self.collisionCheck(xPos, yPos)
        self._pos = [pos[0], pos[1]]        
        
    def collisionCheck(self, xPos, yPos):
        if xPos > self._player_state['draw handler obj']._draw_states['screen width']:
            return (0 , yPos)
        elif xPos < 0:
            return (self._player_state['draw handler obj']._draw_states['screen width'] , yPos)
        elif yPos < 0:
            return (xPos , self._player_state['draw handler obj']._draw_states['screen height'])
        elif yPos > self._player_state['draw handler obj']._draw_states['screen height']:
            return (xPos, 0)
        else:
            return (xPos, yPos)
        
    def reset_pos(self, screen_height, screen_width):
        self._pos = [screen_width/2, screen_height/2]
        
    def get_pos(self):
        self.vel_acc(self._pointing_vector)
        return self._pos

    def update_pting_vector(self, angle):
        self._pointing_vector = angle #need to update  
    
    def update_angle(self, rotationalDirection, angularVelocity, startingAngle):
        #returns final angle by adding initial angle with angularVelocity/change
        if rotationalDirection == "left":
            finalAngle = startingAngle + angularVelocity
        elif rotationalDirection == "right":
            finalAngle = startingAngle - angularVelocity
        else:
            return "Error in update angle"
        return (finalAngle % 360)
        
    #calls the function to update the ships pointing direction
    #updates the ships velocity in the x-y coordinate
    def vel_acc(self, pting_vector):
        if (self._player_state['rotation state'][0] if type(self._player_state['rotation state']) == tuple else False):
            
            rotDirection = self._player_state['rotation state'][1]
            
            shipAngle = self.update_angle(rotDirection,
                                     self._player_state['angular velocity'],
                                     self._player_state['ship angle'])
            
            self._player_state['ship angle'] = shipAngle             
            self._player_state['pointing vector'] = HF.unit_vector(shipAngle)

        if self._player_state['thrust state']:
            pting_vector = self._player_state['pointing vector']
            
            if HF.calc_speed(self._linear_vel) < self._max_linear_vel:
                self._linear_vel[0] += pting_vector[0] * self._linear_acc[0]
                self._linear_vel[1] += pting_vector[1] * self._linear_acc[1]
            
            else:
                self._linear_vel[0] += pting_vector[0] * self._linear_acc[0]
                self._linear_vel[1] += pting_vector[1] * self._linear_acc[1]
            
            self.set_pos()          
            
        elif self._linear_vel[0] != 0 or self._linear_vel[1] != 0:
             updatedVelocity = self.friction_effects(self._linear_vel)
             self._linear_vel = updatedVelocity             
             self.set_pos()
             
             
    def friction_effects(self,linearVelocity):
        finalVelocity = [0.96*linearVelocity[0], 0.96*linearVelocity[1]]
        return finalVelocity
             
             
             
             
             
    
