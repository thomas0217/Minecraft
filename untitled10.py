# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:42:38 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def buildPyramid(x,y,z,block,base)

x,y,z=thomas.player.getTilePos()
base = 18
height = (base//2)+1

for i in range(height):
    x1 = x + i
    y1 = y + i
    z1 = z + i
    
    x2 = x + base - i
    #y與y2相同
    z2 = z + base - i
    mc.setBlocks(x1, y1, z1, x2, y1, z2, 46)
    if 1i=0 and 1i=heigh-1:
        x,y,z =mc.player.getTilePos()
        buildPyarm(x,y,z,46,30)