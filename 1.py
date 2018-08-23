# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:30:37 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()

x,y,z,=thomas.player.getTilePos()
#thomas.player.setPos(x+0.5,y,z+0.5)
while True:
    thomas.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,46)