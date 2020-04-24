import numpy as np
import warnings
from collections import Counter
import pandas as pd
import random

def k_nearest_neighbours(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:
            euclidian_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidian_distance, group])

    votes = [i[1] for i in sorted(distances) [:k]]
    print(Counter(votes) .most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]

    for [i in sorted(distances) [:k]]


    return vote_result

df = pd.read_csv("")