# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

def increment(L):
    return [x+1 for x in L]

def cube(L):
    return [x**3 for x in L]


## 1: (Problem 0.8.3) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    #The Answer showed the beauty of zip, it uses zip a lot to solve the problem
    result = []
    for ta, tb in zip(A, B):
        t = tuple(a+b for a, b in zip(ta, tb))
        result.append(t)
    return result
#    return [tuple(map(sum, zip(*i))) for i in zip(A, B)]



## 2: (Problem 0.8.4) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    return {v:k for k,v in d.items()}



## 3: (Problem 0.8.5) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    result = []
    result.append(p)
    while len(result) < n:
        p += 1
        result.append(p)
    return result

#Couldn't understand what this area is asking us to do
#comprehension_with_row = ...

#comprehension_without_row = ...



## 4: (Problem 0.8.10) Probability Exercise 1
prob  = {1 : 0.5, 2: 0.5, 3: 0.5, 4: 0.1, 5: 0.1, 6:0.1}

#Probability of even number output
v = 0
for x in prob:
    if (x+1) % 2 == 0:
        v += prob[x]

Pr_f_is_even = v

#Probability of odd number output
v = 0
for x in prob:
    if (x+1) % 2 != 0:
        v += prob[x]

Pr_f_is_odd  = v



## 5: (Problem 0.8.11) Probability Exercise 2
values = {1,2,3,4,5,6,7}
prob_dict = {1:0.2, 2:0.2, 3:0.2, 4:0.1, 5:0.1, 6:0.1, 7:0.1}

#Probability of output = 1
v = 0
for x in values:
    if x % 3 == 1:
        v += prob_dict[x]

Pr_g_is_1    = v

#Probability of output = {0, 2}
v = 0
for x in values:
    if x % 3 == 2:
        v += prob_dict[x]
    elif x % 3 == 0:
        v += prob_dict[x]

Pr_g_is_0or2 = v

