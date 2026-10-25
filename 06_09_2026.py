# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:59:59 2026

@author: 91973
"""

import random
position = 0

while position < 100:
    position = position + random.randint(10,30)
    print("Car position:",position)
    
print("Finish")