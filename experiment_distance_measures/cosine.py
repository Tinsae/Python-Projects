# Cosine distance
import numpy as np



	
def cosine_similarity(a, b):
    # find the dot product of a and b
    dot_product = np.dot(a, b)
    # find magnitude of a
    norm_a = np.linalg.norm(a)
    # find maginutude of b
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)
  
  
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print (cosine_similarity(x, y))

