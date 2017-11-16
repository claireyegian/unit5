#Claire Yegian
#11/15/17
#betterColoredWindow.py - better version of coloredWindow.py

from ggame import *
from random import randint

def mouseClick(event):
    changeColor()

def changeColor():
    num1 = randint(0,3)
    
    colorList = ['0x00ff63,1', '0xff4563,1', '0x004300,1', '0xff00ff,1']
    
    color = Color(colorlist[num1])
    colorBox = RectangleAsset(1000,600,LineStyle(1,color),color)
    Sprite(colorBox)

App().listenMouseEvent('click',mouseClick)
App().run()