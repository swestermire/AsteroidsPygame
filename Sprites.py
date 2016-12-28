import pygame

class Sprites:
    '''

    This is the sprite class which will upload and contain all images
    
    File Names:
    asteroid image: asteroid_blue.png
    debris image: debris2_blue.png
    ship image: double_ship.png
    explosion image: explosion_alpha.png
    nebula image: nebula_blue.png
    shot image: shot2.png
    game intro screen image: splash.png
    
    '''
    
    def __init__(self):
        self._game_intro = pygame.image.load("splash.png")
        self._nebula_image = pygame.image.load("nebula_blue.png")
        self._ship_image = pygame.image.load("double_ship.png")
        self._asteroid_image = pygame.image.load("asteroid_blue.png")
        self._shot_image = pygame.image.load("shot2.png")
        
        self._game_images = {'game intro' : self._game_intro,
                             'nebula image' : self._nebula_image,
                             'ship image' : self._ship_image,
                             'asteroid image' : self._asteroid_image,
                             'shot image' : self._shot_image}
                             

    def __getitem__(self, idx):
        return self._game_images[idx]

