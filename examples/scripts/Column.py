""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    4th Ed. by RH Landau, MJ Paez, and CC Bordeianu (D)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2024. 
    Please respect copyright & acknowledge our work."""

# Column.py: Fractal growth of columns

from visual import *;
import random

maxi = 100000;   npoints = 200                # Number iterations, spaces
i = 0;   dist = 0;   r = 0;   x = 0;  y = 0
oldx = 0;   oldy = 0;   pp = 0.0;   prob = 0.0
hit = zeros( (200), int)
graph1 = display(width = 500, height = 500, range=250,        
                 title = 'Correlated Ballistic Deposition')
pts = points(color=color.green, size=2)
for i in range(0, npoints):  hit[i] = 0                     # Clear array
oldx = 100;         oldy = 0
for i in range(1, maxi + 1):
    r = int(npoints*random.random() )
    x = r - oldx
    y = hit[r] - oldy
    dist = x*x  +  y*y
    if (dist ==  0): prob = 1.0         # Sticking prob depends on last x
    else: prob = 9.0/dist
    pp = random.random()
    if (pp < prob):
        if(r>0 and r<(npoints - 1) ):
            if( (hit[r] >=  hit[r - 1]) and (hit[r] >=  hit[r + 1]) ):
                hit[r] = hit[r] + 1
            else:
                if (hit[r - 1] > hit[r + 1]):
                    hit[r] = hit[r - 1]
                else: hit[r] = hit[r + 1]
        oldx = r
        oldy = hit[r]
        olxc = oldx*2 - 200                             # TF for plot  
        olyc = oldy*4 - 200                         
        pts.append(pos=(olxc,olyc))