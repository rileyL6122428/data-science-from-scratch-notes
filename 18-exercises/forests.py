from decision_tree import classify
from collections import Counter

def forest_classify(trees, input):
    votes = [
        classify(tree, input)
        for tree
        in trees
    ]

    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]    