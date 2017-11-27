#Claire Yegian
#11/25/17
#snow.py - creates image of falling snow

from ggame import *

black = Color(0x000000,1)
white = Color(0xffffff,1)

Rectangle = RectangleAsset(400,400,LineStyle(1,black),black)
Rectangle2 = RectangleAsset(400,400,LineStyle(1,black),white)

Sprite(Rectangle)
Sprite(Rectangle2)
App().run()

