#3. Implement in python the following distances

from decimal import Decimal 
from math import *

# calculate the distance between two points
# and takes square root, cuberoot or any other number, rounded
# to three decimal places

def p_root(value, root):
    root_value = 1 / float(root) 
    # round to 3 decimal places
    return round(Decimal(value) ** Decimal(root_value), 3)


def minkowski_distance(x, y, p_value): 
    return (p_root(sum(pow(abs(a-b), p_value) 
            for a, b in zip(x, y)), p_value)) 
            
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Manhattan distance
print(minkowski_distance(x, y, 1))

# Euclidean
print(minkowski_distance(x, y, 2))
    

