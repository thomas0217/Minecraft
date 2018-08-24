# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:22:41 2018

@author: NTPU
"""

form time import sleep
form mcpi.minecraft import Minecraft
thomas = Minecraft.create()
sleep(2)
myID = thomas.getPlayerEntityId("Thomas0217")
thomas.postToTitle(myID,"§you died","§ha ha")