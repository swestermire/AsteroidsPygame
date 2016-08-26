import pygame, Sprites, Players, Physics
import HelperFunctions as HF

class AsteroidsGame(object):
    '''
    This class could theoretically house all the different handlers for this
    particular game, even the physics and game logic.  Not sure what the benefit
    is in this though, other than having everything contained within this one class.
    '''
    def __init__(self):
        print('initializing Asteroids Game...')

    def __str__(self):
        return 'Asteroids Game'
    
    class Event_Handler():
        '''
        Handles player driven actions (i.e. button clicks, mouse clicks, etc.)
        'event_states' is suppose to hold all the event states for a game that is
        driven by player driven events.

        running = if game is on, True, or off, False.
        '''
        
        def __init__(self, player_obj):
            print('Initializing Asteroids Event Handler...')
            self._event_states = {'running': True}
            self._player_obj = player_obj

        def action(self, event, draw_handler_obj):
            if event.type == pygame.QUIT:
                print('Game Shutdown')
                self._event_states['running'] = False #this turns off the game

            elif event.type == pygame.KEYDOWN:  #handler for key press down events

                if event.key == pygame.K_LEFT:
                    self._player_obj._rotation_state = True

                elif event.key == pygame.K_RIGHT:
                    
                    return
                    
                elif event.key == pygame.K_UP:
                    self._player_obj.thrust_on_off('on')

                elif event.key == pygame.K_DOWN:
                    return

            elif event.type == pygame.KEYUP:  #handler for key up events

                if event.key == pygame.K_LEFT:
                    self._player_obj._rotation_state = False

                elif event.key == pygame.K_RIGHT:
                    return

                elif event.key == pygame.K_DOWN:
                    return

                elif event.key == pygame.K_UP:
                    self._player_obj.thrust_on_off('off')

            elif event.type == pygame.MOUSEBUTTONUP:
                if draw_handler_obj.get_draw_state('screen state')  == 'blank screen':
                    draw_handler_obj['screen state'] = 'game intro'
                elif draw_handler_obj.get_draw_state('screen state') == 'game intro':
                    draw_handler_obj['screen state'] = 'main game'
            
        def __getitem__(self, item):
            return self._event_states[item]
        
    class Draw_Handler():
        '''
        This will draw the objects on the game to the user.
        '''

        def __init__(self, sprite_obj, player_obj, height = 700, width = 700):
            print('Initializing Asteroids Draw Handlers...')
            self._sprite_obj = sprite_obj
            self._player_obj = player_obj
            self._screen = pygame.display.set_mode((height,width))
            self._draw_states = {'screen height': height,
                                 'screen width': width,
                                 'screen state': 'blank screen'}
                                     
            self._sized_game_intro = pygame.transform.scale(self._sprite_obj['game intro'],
                                                            (self._draw_states['screen height'],
                                                            self._draw_states['screen width']))

            self._sized_nebula = pygame.transform.scale(self._sprite_obj['nebula image'],
                                                        (self._draw_states['screen height'],
                                                         self._draw_states['screen width']))

            self._clipped_ship = self._sprite_obj['ship image']
            self._clipped_ship.set_clip(pygame.Rect(0,0,90,90))
            self._ship_surface = self._clipped_ship.subsurface(self._clipped_ship.get_clip())

            self._player_obj.reset_pos(self._draw_states['screen height'],
                                 self._draw_states['screen width'])            
            
        def game_state(self, mode):
            '''
            game_state method will control what images, windows, layouts are drawn to the user.
            (i.e. game menu, start screen, the main game, high score rankings, etc.)
            '''
            if mode == 'blank screen':
                return self._screen.fill((255,255,255))
            elif mode == 'game intro':
                return self._screen.blit(self._sized_game_intro, (0,0))
            elif mode == 'main game':
                self._screen.blit(self._sized_nebula, (0,0))

                self.update_rotated_image(self._ship_surface, self._player_obj)
                self._screen.blit(self._ship_surface, self._player_obj.get_pos())
                return self._screen

        def update_rotated_image(self, surface, obj):
            if obj._rotation_state:
                self._ship_surface = pygame.transform.rotate(surface, HF.pting_vector_angle(obj._pointing_vector))
            
        def get_draw_state(self, idx):
            return self._draw_states[idx]
        
        def __getitem__(self, idx):
            return self.game_state(self._draw_states['screen state'])

        def __setitem__(self, key, value):
            '''
            this sets value as it relates to the draw states
            This will also readjust all images based on screen size when a screen property is changed.
            '''
            self._draw_states[key] = value

            if key == 'screen width' or key == 'screen height':
                self._sized_game_intro = pygame.transform.scale(self._sprite_obj['game intro'],
                                                             (self._draw_states['screen height'],
                                                              self._draw_states['screen width']))
                
                self._sized_nebula = pygame.transform.scale(self._sprite_obj['nebula image'],
                                                            (self._draw_states['screen height'],
                                                             self._draw_states['screen width']))
            elif value == 'main game':
                return
                


### Main Game Program ###
pygame.init()
def main():
            
    #initializing game objects
    sprite_obj = Sprites.Sprites()
    player_obj = Players.Player()
    
    event_handler_obj = AsteroidsGame.Event_Handler(player_obj)
    draw_handler_obj = AsteroidsGame.Draw_Handler(sprite_obj, player_obj)
    
    state = 'blank screen'
    
    while event_handler_obj['running']:

        for event in pygame.event.get():
            '''
            instead of having a huge number of if branches to assess the events, maybe
            we can pass the event to an event handler which returns a dictionary/hash table
            that describes the state of the game/player (i.e. {game_state: True, player_health: 100, etc...})
            '''
            event_handler_obj.action(event, draw_handler_obj)
            
        draw_handler_obj['']
        
        pygame.display.flip()
        
    pygame.quit()

        
main()