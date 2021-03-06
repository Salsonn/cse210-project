from game.point import Point
from game.math import *
from game.add_entity import add_entity
import arcade
from game import constants

class Weapon(arcade.Sprite):
    def __init__(self, check_flip, position, weaponType, weaponDamage, weaponRate, weaponImage):
        super().__init__(weaponType, center_x = 0, center_y = 0, flipped_horizontally=True, flipped_vertically=check_flip, scale = 1.25)
        # self.weapons = constants.weaponImages
        self._power = weaponDamage
        self._cooldown = weaponRate
        self.center_x = position[0]
        self.center_y = position[1]
        self.angle = 0
        self.counter = 0
        # if weaponType == 1:
        self._projectileBounces = 0
        self._image = weaponImage

        # image, scale, image_x, image_y, image_width, image_height, center_x,center_y

    def inputCheck(self, entities, reticle, input_service):
        player = entities["player"][0]
        wTheta = round(self.angle, 3)
        if input_service.check_click():
            if self.counter % self._cooldown == 0:
                add_entity(entities, "projectile", Point(self.position[0], self.position[1] - 4), theta(Point(player.center_x, player.center_y), reticle.get_reticle()), self._projectileBounces, self._power)
            self.counter += 1

    def flip(self):
        if self.cartesian in {2, 3}: return True
        else: return False
    
    def flipH(self, flipped):
        self.texture = self._image[flipped]

    # WEAPON PICKUP NOT IMPLEMENTED UNTIL FURTHER NOTICE

    # def weapon_pickup(self, fallen_weapon_x, fallen_weapon_y, player_x, player_y):
    #     '''
    #     Runs when the user picks up a dropped weapon.

    #     It then switches their weapon out for the picked up weapon
    #     '''
    #     distance_x = abs(player_x - fallen_weapon_x)
        
    #     distance_y = abs(player_y - fallen_weapon_y)
        
    #     if distance_x <= 5 and distance_y <= 5:
            
    #         # If returned True, then the weapon is within 
    #         # reasonable range to be picked up
    #         return True

    #     # If returned false, the weapon is too far away to be picked up
    #     return False
    
    def update_weapon_angle(self, playerX, playerY, mouseX, mouseY):
        '''
        Checks the current coordinates of the player and moves the weapon to
        stay in its standard position so that it's not stationary

        > Moves according to Character Position <
        '''
        self.cartesian = cartesian(mouseX, mouseY, playerX, playerY)

        finalX = abs(playerX - mouseX)
        finalY = abs(playerY - mouseY)
        h = hypotenuse(finalX, finalY)
        av = angle(h, finalY)
        theta = direction(self.cartesian, av)
        
        return theta

        