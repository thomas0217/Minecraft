# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:59:27 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()
import time,random
x,y,z,=thomas.player.getTilePos()
while True:
    color =random.randrange(1,16)
    thomas.setBlocks(x+100,y-1,z+100,x-100,y-1,z-100,95,color)
    time.sleep(1)