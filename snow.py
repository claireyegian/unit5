#Claire Yegian
#11/25/17
#snow.py - creates image of falling snow

from ggame import *
from random import randint

def step():
    for item in flakeList:
        Sprite(item)
        item.y += 1
        if item.y > 15:
                step()
    
if __name__ == '__main__':
    black = Color(0x000000,1)
    white = Color(0xffffff,1)
    
    rectangle = RectangleAsset(400,400,LineStyle(1,black),black)
    snowflake = RectangleAsset(5,5,LineStyle(1,white),white)
    
    Sprite(rectangle)
    flakeList = []
    for i in range (0,100):
        flakeList.append('snowflake,(randint(0,400),0)')
        i += 1
    App().run(step)