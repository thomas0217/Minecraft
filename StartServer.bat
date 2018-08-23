# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:06:31 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()
x,y,z,=thomas.player.getTilePos()

width=10
length=10
height=4
thomas.setBlocks(x,y,z,x+width,y+height,z+length)
thomas.setBlicks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1)