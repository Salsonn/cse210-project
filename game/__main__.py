import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.environment_action import EnvironmentAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService
from game.reticle import Reticle

from game.entity.player import Player
from game.entity.enemy import Enemy
from game.entity.weapon import Weapon
from game.entity.drop import Drop
from game.entity.trigger import Trigger

from game.director import Director
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # create the player and place in default location
    player = Player((640, 360), False)
    cast["player"] = [player]

    # create empty list of projectiles, will be populated automatically later
    cast["projectile"] = []

    # create the first weapon, will automatically position near the player
    weapon1 = Weapon(False, (640, 360), constants.weaponImagePath1, constants.weaponDamages[0], constants.weaponRates[0], constants.weapon1Image)
    weapon2 = Weapon(False, (640, 360), constants.weaponImagePath2, constants.weaponDamages[1], constants.weaponRates[1], constants.weapon2Image)
    cast["weapon"] = [weapon1, weapon2]

    # create empty list of collidable walls, will be populated and drawn by the map code
    cast["wall"] = []

    # create empty list of triggers, will be populated by maps
    cast["trigger"] = []

    # create empty list of enemies, will be populated on map load
    cast["enemy"] = []

    # create a medkit to reset the player health to max value
    cast["drop"] = []

    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()

    reticle = Reticle()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    draw_actors_action = DrawActorsAction(output_service, cast)
    handle_collisions_action = HandleCollisionsAction(draw_actors_action)
    environment_action = EnvironmentAction(cast)

    
    script["input"] = [control_actors_action]
    script["update"] = [environment_action, handle_collisions_action, move_actors_action]
    script["output"] = [draw_actors_action]

    # start the game
    batter = Director(cast, script, input_service, reticle)
    batter.setup()
    arcade.run()


if __name__ == "__main__":
    main()