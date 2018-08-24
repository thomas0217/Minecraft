# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:13:25 2018

@author: NTPU
"""

form time import sleep
form mcpi.minecraft import Minecraft
thomas = Minecraft.create()
block=[46+,46]
r = choice(block)
myID = thomas.getPlayerEntityId("Thomas0217")
x,y,z=thomas.entity.getTilePos(myID)
thomas.setBlock(x,y,z,r)