import arcade
from game import constants
from game.entity.trigger import Trigger

class Gameover:

    def __init__(self, levelController, entities, playerScore):
        
        self._triggers = entities["trigger"]
        self._collidableWalls = entities["wall"]
        self._enemies = entities["enemy"]
        self._drops = entities["drop"]
        self._levelController = levelController

        self._BACKGROUND_COLOR = arcade.color.BLACK
        self._GAME_OVER_COLOR = arcade.color.RED_DEVIL
        self._SCORE_COLOR = arcade.color.BLUE_YONDER
        self._SCORE_TEXT_COLOR = arcade.color.UFO_GREEN
        self._CONTINUE_COLOR = arcade.color.FERN_GREEN
        self._DISMISS_COLOR = arcade.color.REDWOOD

        self._TITLE = 'GAME OVER'
        self._FINAL_SCORE = 'TOTAL SCORE'
        self._SCORE = str(playerScore)
        self._TRY_AGAIN = 'TRY AGAIN?'

        self._CONTINUE = 'YES'
        self._DISMISS = 'NO'

        # self._ARCH = './images/catacombs/cata_v1.0/mainlevbuild.png'
        self._ARCH = 'game\\images\\catacombs\\cata_v1.0\\mainlevbuild.png'
        self._COLUMN_SPACING = 20
        self._ROW_SPACING = 20
        self._LEFT_MARGIN = 110
        self._BOTTOM_MARGIN = 110
        self._TILE_SPACING = 1.6

    def load(self):
        self._drops.clear()
        self._triggers.clear()
        self._collidableWalls.clear()
        self._enemies.clear()
        # self.prepare_floor()

    def drawMap(self, playerScore):
        self._SCORE = str(playerScore)
        self.draw_instructions()
        self.draw_doors()
        self.draw_messages()
    
    def draw_instructions(self):
        arcade.draw_text(self._TITLE, constants.windowX / 2 - 225, constants.windowY / 2, self._GAME_OVER_COLOR, 72, 450, 'center', 'calibri', True)
        arcade.draw_text(self._FINAL_SCORE, constants.windowX / 2 - 360, constants.windowY / 2 - 45, self._SCORE_TEXT_COLOR, 42, 720, 'center', 'calibri', True)
        arcade.draw_text(self._SCORE, constants.windowX / 2 - 200, constants.windowY / 2 - 100, self._SCORE_COLOR, 42, 400, 'center', 'calibri', True)
        arcade.draw_text(self._TRY_AGAIN, constants.windowX / 2 - 280, constants.windowY / 2 + 225, self._SCORE_COLOR, 50, 560, 'center', 'calibri', True)
        # arcade.draw_text(self._TRY_AGAIN, constants.windowX / len(self._LINE2) + 350, constants.windowY - 160, self._FONT_COLOR, 25, 560, 'center', 'calibri', True)
        
    def draw_doors(self):
        # Draw Arch for Main MENU
        archYes = arcade.Sprite(self._ARCH, 1, 398.0, 14.0,84,93)
        archYes.center_x = 4 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 80
        archYes.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 405
        archYes.draw()

        level1Loader = Trigger(archYes.center_x, archYes.center_y + 20, 80, 76, self, 1)
        self._triggers.append(level1Loader)

        # Draw Arch for Level 1
        archNo = arcade.Sprite(self._ARCH, 1, 398.0, 14.0,84,93)
        archNo.center_x = 31 * (self._COLUMN_SPACING * self._TILE_SPACING) + (self._LEFT_MARGIN * self._TILE_SPACING) - 84
        archNo.center_y = (self._ROW_SPACING * self._TILE_SPACING) + (self._BOTTOM_MARGIN * self._TILE_SPACING) + 405
        archNo.draw()
        
        quitTrigger = Trigger(archNo.center_x, archYes.center_y + 20, 80, 76, self, 2)
        self._triggers.append(quitTrigger)

    def draw_messages(self):
        # Draw Level 1  text for Arch
        arcade.draw_text(self._CONTINUE, 55, constants.windowY - 60, self._CONTINUE_COLOR, 20, 340, 'center', 'calibri', True)
        
        # Draw Main Menu  text for Arch
        arcade.draw_text(self._DISMISS, constants.windowX - 370, constants.windowY - 60, self._DISMISS_COLOR, 20, 340, 'center', 'calibri', True)

        
    def handleTrigger(self, actionIndex):
        if actionIndex == 1:
            self._levelController.changeLevel(-1)
        elif actionIndex == 2:
            exit()