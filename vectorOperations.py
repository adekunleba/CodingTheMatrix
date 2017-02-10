# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:38:07 2017

@author: ADEKUNLE
"""

#The Vector
#KEY POINT: Think Vector as a function
#Vector Addition ---
#E.g:
def add2(v, w):
    return[v[0] + w[0], v[1] + w[1]]

add2((3, 4), (5,6))
#
#Quiz:Write a function that says 'go east one mile, go north two mile
def go_plus_one(e,n):
    return (e+1, n+2)


go_plus_one(4,4)
go_plus_one(-4, -4) 
#Translating the above to describe vector/function as a carrier
#We say it carries (4,4) to (5,6) or ((3,4), (5,6)) to (8, 10)
#Quiz: Write a function that takes 2 n-vector list and add them together
def addn(v, w):
    return[v[i] + w[i] for i in range(len(v))]

#Also you can use zip to solve same question. Zip brings togeter the ith
#....element of each vector into a tuple and then you can add with alist comprehension
def addn(v, w):
    return[x+y for (x,y) in zip(v,w)]

v = list(range(10))
w = list(range(4,24,2))

addn(v,w)

#Scalar-Vector Multiplication
def scalar_vector_mult(alpha, v):
    return[alpha * value for value in v]
    

scalar_vector_mult(3, v)

#A more stable and generalized function will be
def scalar_vector_mult(alpha, v):
    return[alpha * v[i] for i in range(len(v))] 

#Scalar Multiplication and addition will follow bodmas
def scalar_vector_mult_add(alpha, v, w):
    return[alpha * v[i] + w[i] for i in range(len(v))]

#Task Write a python procedure segment(pt1, pt2) that, given points represented as
#2-element lists, returns a list of a hundred points spaced evenly along 
#the line segment whose endpoints are the two points
def segment(pt1, pt2):
    period = 100
    list_val = []
    for i in range(period):
        alpha = (1.0/period) * i
        beta = 1 - alpha
        x = alpha * pt1[0] + beta * pt2[0]
        y = alpha * pt1[1] + beta * pt2[1]        
        list_val.append((x, y))
    return list_val

list_val = segment([3.5, 3], [0.5, 1])

from plotting import plot

plot(list_val, 4)