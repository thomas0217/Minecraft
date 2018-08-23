# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:48:27 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()
 x,y,z=thomas.player.getTilePos()
 
a=thomas.getBlocks(x+1,y-1,z)
a=thomas.getBlocks(x-1,y-1,z)
a=thomas.getBlocks(x,y-1,z+1)
a=thomas.getBlocks(x,y-1,z-1)

if a==8 or a==9 b==8 or b==9 c==8 or c==9 d==8 or d==9:
    thomas.setblocks(x+1,y-1,z+1,x-1,y-1,z-1,46)