import math

def compute_y(x):
   
    return math.sqrt(1 + math.cos(x**2 + x) + x**4)

def compute_sum(x, h, N):
   
    return (x + h) * N * (N + 1) / 2
