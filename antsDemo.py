#Claire Yegian
#11/20/17
#antsDemo.py - how to use lists with graphics

from ggame import *
from random import randint

WIDTH = 1000 #constant throughout program so in all caps
HEIGHT = 600

if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    data = {}
    data['antList'] = []
    
    for i in range(10):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run()
