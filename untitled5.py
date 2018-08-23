# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:45:18 2018

@author: NTPU
"""


from mcpi.minecraft import Minecraft
thomas=Minecraft.create()


while True:
    hits = thomas.events.pollProjectileHits()
    if len(hits)>0:
        h =hits[0]
        x,y,z =h.pos.x,h.pos.y,h.pos.z
        thomas.createExplosion(x,y,z,100)
        #block = thomas.getBlock(x,y,z)
        #mc.postToChat("恭喜你獵到"+str(block))
        
        
    
