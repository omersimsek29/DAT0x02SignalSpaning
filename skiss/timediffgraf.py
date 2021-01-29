# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:42:11 2021

@author: pennz
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import turtle


circle1 = plt.Circle((0, 0), 0.33, color='r', fill = False)
circle2 = plt.Circle((0, 2), 0.33, color='blue', fill = False)
circle3 = plt.Circle((2, 2), 0.33, color='g', fill = False)
circle4 = plt.Circle((2, 0), 0.33, color='grey', fill = False)

circle5 = plt.Circle((0, 0), 0.66, color='r', fill = False)
circle6 = plt.Circle((0, 2), 0.66, color='blue', fill = False)
circle7 = plt.Circle((2, 2), 0.66, color='g', fill = False)
circle8 = plt.Circle((2, 0), 0.66, color='grey', fill = False)

circle9 = plt.Circle((0, 0), 0.99, color='r', fill = False)
circle10 = plt.Circle((0, 2), 0.99, color='blue', fill = False)
circle11 = plt.Circle((2, 2), 0.99, color='g', fill = False)
circle12 = plt.Circle((2, 0), 0.99, color='grey', fill = False)

circle13 = plt.Circle((0, 0), 1.33, color='r', fill = False)
circle14 = plt.Circle((0, 2), 1.33, color='blue', fill = False)
circle15 = plt.Circle((2, 2), 1.33, color='g', fill = False)
circle16 = plt.Circle((2, 0), 1.33, color='grey', fill = False)

circle17 = plt.Circle((0, 0), 1.66, color='r', fill = False)
circle18 = plt.Circle((0, 2), 1.66, color='blue', fill = False)
circle19 = plt.Circle((2, 2), 1.66, color='g', fill = False)
circle20 = plt.Circle((2, 0), 1.66, color='grey', fill = False)

circle21 = plt.Circle((0, 0), 2, color='r', fill = False)
circle22 = plt.Circle((0, 2), 2, color='blue', fill = False)
circle23 = plt.Circle((2, 2), 2, color='g', fill = False)
circle24 = plt.Circle((2, 0), 2, color='grey', fill = False)

circle25 = plt.Circle((0, 0), 2.33, color='r', fill = False)
circle26 = plt.Circle((0, 2), 2.33, color='blue', fill = False)
circle27 = plt.Circle((2, 2), 2.33, color='g', fill = False)
circle28 = plt.Circle((2, 0), 2.33, color='grey', fill = False)


circle29 = plt.Circle((0, 0), 2.66, color='r', fill = False)
circle30 = plt.Circle((0, 2), 2.66, color='blue', fill = False)
circle31 = plt.Circle((2, 2), 2.66, color='g', fill = False)
circle32 = plt.Circle((2, 0), 2.66, color='grey', fill = False)
    
ax = plt.gca()
ax.cla() # clear things for fresh plot

# change default range so that new circles will work
ax.set_xlim((0, 2))
ax.set_ylim((0, 2))
# some data

# key data point that we are encircling

    
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(circle4)
ax.add_patch(circle5)
ax.add_patch(circle6)
ax.add_patch(circle7)
ax.add_patch(circle8)

ax.add_patch(circle9)
ax.add_patch(circle10)
ax.add_patch(circle11)
ax.add_patch(circle12)

ax.add_patch(circle13)
ax.add_patch(circle14)
ax.add_patch(circle15)
ax.add_patch(circle16)

ax.add_patch(circle17)
ax.add_patch(circle18)
ax.add_patch(circle19)
ax.add_patch(circle20)

ax.add_patch(circle21)
ax.add_patch(circle22)
ax.add_patch(circle23)
ax.add_patch(circle24)

ax.add_patch(circle25)
ax.add_patch(circle26)
ax.add_patch(circle27)
ax.add_patch(circle28)

ax.add_patch(circle29)
ax.add_patch(circle30)
ax.add_patch(circle31)
ax.add_patch(circle32)
