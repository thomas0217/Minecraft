e# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:15:27 2018

@author: NTPU
"""

form random import randrange
from mcpi.minecraft import Minecraft
thomas = Minecraft.create()


for i in range(10):
    x,y,z = thomas.player.getTilePos()
    x=x+j
    for i in range(30):
        r = randrange(0,16)
        thomas.setBlock(x,y,z,35,r)
        z=z+1
thomas.postToChat("請找出隱藏方塊")
r = randrange(0,16)
while True:
    hits = thomas.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        
        block = thomas.getBlockWithData(h.pos)
        datd = block.data
        if data==r:
            thomas.postToChat("找到了")
            thomas.setBlock(h.pos,57)
            break
        if data>r:
            thomas.postToChat("要找更小的")
            if data<r:
            thomas.postToChat("要找更大的")
        
        