# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:06:32 2018

@author: NTPU
"""


from mcpi.minecraft import Minecraft
thomas=Minecraft.create()
x,y,z=thomas.player.getTilePos()
thomas.setSign(x,y,z,63,0,"fortine","minecraft","版","")