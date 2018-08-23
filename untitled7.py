# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:33:28 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas=Minecraft.create()

pos = thomas.player.getTilePos
while True:
    x=pos.x+random.uniform(-50,50)
    y=pos.y+40
    z=pos.z=random.uniform(-50,50)
    thomas.spawnEntity(x,y,z,63)
    time.sleep(0.1)