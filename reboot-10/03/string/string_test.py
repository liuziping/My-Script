#!/usr/bin/env python
import os
filenames = []   
for filename in os.listdir('/home/liuziping/03'):
    if filename.endswith(".py"):
           file = filename.rstrip(".py")
           filenames.append(file)
print filenames




