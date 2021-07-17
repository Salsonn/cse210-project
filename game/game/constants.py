import os
import arcade
import random

windowX = 1280
windowY = 720

movementSpeed = 5 # Pixels per frame
projectileSpeed = 30

blueEnemySpeed = random.randrange(5, 6)
yellowEnemySpeed = random.randrange(3, 5)
redEnemySpeed = random.randrange(2, 3)

blueEnemyDamage = 2
yellowEnemyDamage = 4
redEnemyDamage = 6

blueEnemyPoints = 60
yellowEnemyPoints = 40
redEnemyPoints = 30

playerScore = 0
playerHealth = 100

tickSpeed = 120

enemyTopRandom = {'min_x': 100, 'max_x': 1000, 'min_y': 450, 'max_y': 575}
enemyBottomRandom = {'min_x': 100, 'max_x': 1000, 'min_y': 75, 'max_y': 150}
enemyLeftRandom = {'min_x': 75, 'max_x': 150, 'min_y': 75, 'max_y': 575}
enemyRightRandom = {'min_x': 950, 'max_x': 1100, 'min_y': 75, 'max_y': 575}

acceleration = 2 # Pixels per frame per frame

dropsImage = "game\\images\\medkit_sprite.png"
playerImage = "game\\images\\characters\\Player.gif"
projectile1Image = "game\\images\\bullet.png"
enemyImages = ["game\\images\\characters\\Enemy.gif", "game\\images\\characters\\Enemy2.gif", "game\\images\\characters\\Enemy3.gif"]
weaponImage = "game\\images\\weapons\\ak.png"

# menuMusic = "game\\sounds\\background.mp3"
menuMusic = "game\\sounds\\CoconutMall.mp3"
levelMusic = "game\\sounds\\ангел.mp3"

mute = False
# Music length in seconds
menuMusicLength = 127

debug = False
collisionDebug = False