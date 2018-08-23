# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:17:58 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
thomas = Minecraft.create()

import sleep
while True:
    thomas.executeCommand("time add 10")
    time.sleep(0.1)