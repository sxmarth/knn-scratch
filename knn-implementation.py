import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k': [[1,2], [2,3], [3,1]], 'r': [[6,5],[7,7],[8,6]]}
new_features = [5,7]

def k_nearest_neighbours(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:


    return vote_result