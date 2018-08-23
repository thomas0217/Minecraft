# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:23:12 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas = Minecraft.create()
nunber = 1
x,y,z = thomas.player.getTilePos()
for i in range(number):
    thomas.spawnEntity(x,y,z,46)
number = nunber*2

