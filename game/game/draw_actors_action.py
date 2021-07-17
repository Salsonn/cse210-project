from game.maps.menu import MainMenu
from game.maps.welcome import Welcome
from game.maps.level1 import Level1
from game.maps.instructions import Instructions

from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service, entities):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self._mainMenu = MainMenu(self, entities)
        self._welcome = Welcome(self, entities)
        self._instructions = Instructions(self, entities)
        self._level1 = Level1(self, entities)
        self.changeLevel(-1)

    def execute(self, entities, reticle, current_level):
        """Executes the action using the given actors.

        Args:
            entities (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        #for ball in entities["balls"]:
        #    self._output_service.draw_actor(ball)

        if self._activeLevel == -1:
            self._welcome.drawMap(reticle)
            return self._activeLevel
        elif self._activeLevel == -2:
            self._instructions.drawMap()
        elif self._activeLevel == 1:
            self._level1.drawMap(entities["player"][0])
        elif self._activeLevel == 0:
            self._mainMenu.drawMap()

        player = entities["player"][0] # there's only one
        self._output_service.draw_actor(player)
        
        weapon = entities["weapon"][0]
        self._output_service.draw_actor(weapon)
        
        if self._activeLevel == 1:
            for enemy in entities["enemy"]:
                self._output_service.draw_actor(enemy)

        if self.activeLevel == 1:
            for drop in entities["drops"]:
                self._output_service.draw_actor(drop)
        
        for projectile in entities["projectile"]:
            self._output_service.draw_actor(projectile)

        self._output_service.flush_buffer()

        return self._activeLevel

    def changeLevel(self, newLevel):
        self._activeLevel = newLevel
        constants.currentLevel = self._activeLevel
        if newLevel == -1:
            self._welcome.load()
        elif newLevel == 0:
            self._mainMenu.load()
        elif newLevel == 1:
            self._level1.load()
        elif newLevel == -2:
            self._instructions.load()
        
        return self._activeLevel

    def getLevel(self):
        return self._activeLevel