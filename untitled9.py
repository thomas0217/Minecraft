# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:39:42 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()

x,y,z=thomas.player.getTilePos()
for i in range(87):
    thomas.setBlock(x,y-1,z+i,46)