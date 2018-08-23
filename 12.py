# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:26:07 2018

@author: NTPU
"""
import random
from mcpi.minecraft import Minecraft
thomas = Minecraft.create()
x,y,z=thomas.player.getTilePos()
for i in range(20):
    r=random.randrange(1,9)
    c=random.randrange(1,16)
    l=random.randrange(2,16)
    if r==1:
        thomas.setBlocks(x,y,z,x+4,y,z,46)
    if r==2:
        thomas.setBlocks(x,y,z,x-4,y,z,46)
    if r==3:
        thomas.setBlocks(x,y,z,x,y,z+4,46)
    if r==4:
        thomas.setBlocks(x,y,z,x,y,z-4,46)
    if r==5:
        thomas.setBlocks(x,y,z,x,y+1,z,46)
    if r==5:
        thomas.setBlocks(x,y,z,x,y-1,z,46)