# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 06:30:59 2017

@author: ADEKUNLE
"""

#Working with Complex Numbers
S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.25 + 1j, 2.75 + 1j, 3.25 + 1j}

#Given a plot function plot S

from plotting import plot

plot(S, 4)

#Adding Complex Nubers
plot((1+2j+z for z in S), 4)

#Multiplication of complex numbers with 0.5 reduces spaces between the points
plot((0.5*z for z in S), 4)

#To rotate the points by 180 degree we multiply by (-1)
plot((-1*z for z in S), 4)

#To rotate by 180 degree we multiply by 1i equivalent to 1j in python
plot((1j * z for z in S), 4)
plot((0.5j * z for z in S), 4) #rotate by 180 and reduce space btw points

#create a new plot in which the points of S are rotated by 90 degrees, scaled 
#by 1/2, and then shifted down by one unit and to the right two units
plot((2 - 1j + (0.5j * z) for z in S), 4)  #Also gives correct answer
plot(((z*1j/2)+2-1j for z in S), 4) #Correct answer

#Given an image img.png
from image import *
file = file2image("img01.png")

#Calculat the height and width of image
r = len(file) #gives the height
c = len(file[0]) #Gives the width

pts = [x+(r-y)*1j for x in range(c) for y in range(r)[::-1] for \
       intensity in file[y][x] if intensity < 120]

#Plotting the image
plot(pts, r)

#Function z map to S to center S to the origin
