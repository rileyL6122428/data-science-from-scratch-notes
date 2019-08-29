from collections import Counter
from math import sqrt
from functools import reduce

def majority_vote(labels):
    # ASSUME LABELS ARE ORDERED FROM NEAREST TO FARTHEST
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([
        count
        for count 
        in vote_counts.values()
        if count == winner_count
    ])
    return winner if num_winners == 1 else majority_vote(labels[:-1])

def add(num_a, num_b):
    return num_a + num_b

def squared_difference(num_a, num_b):
    return (num_a - num_b) ** 2

def distance(vector_a, vector_b):
    squared_differences = map(squared_difference, vector_a, vector_b)
    sum_of_squared_differences = reduce(add, squared_differences)
    return sqrt(sum_of_squared_differences)

def knn_classify(k, labeled_points, new_point):
    # labeled points have structure (point, label)
    
    by_distance = sorted(
        labeled_points,
        key=lambda coord_lang_pair: distance(coord_lang_pair[0], new_point)
    )

    k_nearest_labels = [
        label
        for _, label
        in by_distance[:k]
    ]

    return majority_vote(k_nearest_labels)
