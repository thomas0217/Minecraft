# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:14:25 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()
x,y,z=thomas.player.getTilePos()

width=100
length=100
height=100
thomas.setBlocks(x,y,z,x+width,y+height,z+length,46)
thomas.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,46)