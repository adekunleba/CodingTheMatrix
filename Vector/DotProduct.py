# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:16:39 2017

@author: ADEKUNLE
"""

###########DOT PRODUCT EXERCISES#################
def get_item(v, d):
    """
    Returns the value of an element(domain) in Vec v
    """
    return v.f[d] if d in v.f else 0



def list_dot(u, v):
    """
    Takes two equal length list u, v an 
    
    Return the dot product of u, v interpreted as vector
    """
    return sum([u[i]*v[i] for i in range(len(u))])
    #You can use zip also
    #return sum([a*b for (a,b) in zip(u,v)])

###Explaining Total Cost of Benefit using Vec
from vec import Vec

##Given D as a set of ingreddient for making beers
D = {'hops', 'malt', 'water', 'yeast'}
cost = Vec(D, {'hops' : 2.50, 'malt' : 1.50, 'water' : 0.006, 'yeast' : 0.45})

quantity = Vec(D, {'hops':6, 'malt':14, 'water':7, 'yeast':11})
#
#TASK:
    #Given a set of values, and a Cost class and quantity
    #Define a function to do list_dot product
def do_calc(class1, class2, D):
    """
    class1 is a class defined by Vec
    class2 class defined by Vec
    D set of values common to class1 and class2
    """
    class1_val = []
    for i in D:
        class1_val.append(get_item(class1, i))
    
    class2_val = []
    for i in D:
        class2_val.append(get_item(class2, i))
    list_dot_val = list_dot(class1_val, class2_val)
    return list_dot_val

cost_quantity = do_calc(cost, quantity, D)
#Out[70]: 40.992000000000004

value =  Vec(D, {'hops' : 0, 'malt' : 960, 'water' : 0, 'yeast' : 3.25})

quantity_value = do_calc(quantity, value, D)
#Out[72]: 13475.75