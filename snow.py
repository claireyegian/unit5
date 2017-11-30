#Claire Yegian
#11/25/17
#snow.py - creates image of falling snow

from ggame import *
from random import randint

def step():
    flake = Sprite(snowflake,(randint(0,400),0))
    data[flakeList].append(flake)
    for item in data[flakeList]:
        item.y += 1
        if item.y > 15:
                step()
    
if __name__ == '__main__':
    
    data = []
    data[flakeList = []]
    
    black = Color(0x000000,1)
    white = Color(0xffffff,1)
    
    rectangle = RectangleAsset(400,400,LineStyle(1,black),black)
    snowflake = RectangleAsset(5,5,LineStyle(1,white),white)
    
    Sprite(rectangle)
    App().run(step)