# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:34:23 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()
 x,y,z=thomas.player.getTilePos()
 
a=0
while a<30:
    thomas.setBlock(x,y-1,z+30,x,y-30,z-30,46)