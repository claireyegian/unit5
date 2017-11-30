#Claire Yegian
#11/25/17
#snow.py - creates image of falling snow

from ggame import *
from random import randint

black = Color(0x000000,1)
white = Color(0xffffff,1)

rectangle = RectangleAsset(400,400,LineStyle(1,black),black)
snowflake = RectangleAsset(5,5,LineStyle(1,white),white)

Sprite(rectangle)
Sprite(snowflake,(randint(0,400),0))
App().run()

