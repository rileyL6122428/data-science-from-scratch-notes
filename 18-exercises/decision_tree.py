from collections import defaultdict
from entropy import partition_entropy
from interview_data import inputs
from functools import partial

def partition_by(inputs, attribute):
    groups = defaultdict(list)

    for input in inputs:
        attributes = input[0]
        value = attributes[attribute]
        groups[value].append(input)
        
    return groups

def partition_entropy_by(inputs, attribute):
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())

# for attribute in ['level', 'lang', 'tweets', 'phd']:
#     print(attribute, partition_entropy_by(inputs, attribute))

# Level Attribute yields the lowest entropy/ highest information gain

senior_inputs = [
    (input, label)
    for input, label
    in inputs
    if input['level'] == 'Senior'
]
    
# print('Senior Dev Entropies')
# for attribute in ['lang', 'tweets', 'phd']:
#     print(attribute, partition_entropy_by(senior_inputs, attribute))

# Lowest entropy for senior devs is tweets, 
# which totally predicts if they interview well

junior_inputs = [
    (input, label)
    for input, label
    in inputs
    if input['level'] == 'Junior'
]
# print('junior dev Entropies')
# for attribute in ['lang', 'tweets', 'phd']:
#     print(attribute, partition_entropy_by(junior_inputs, attribute))

# The inverse of has phd predicts interview success

# Our Tree:
our_id3_tree = ('level', {
    'Junior': 
        ('phd', {
            'yes': False,
            'no': True,
        }),

    'Mid': True,

    'Senior': 
        ('tweets', {
            'yes': True,
            'no': False
        })
})

def classify(tree, input):
    if tree in [True, False]:
        return tree
    else:
        attribute, subtree_dict = tree
        subtree_key = input.get(attribute)

        if subtree_key not in subtree_dict:
            subtree_key = None

        subtree = subtree_dict[subtree_key]
        return classify(subtree, input)


def build_tree_id3(inputs, split_candidates=None):
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()

    num_inputs = len(inputs)
    num_trues = len([ label for item, label in inputs if label ])
    num_falses = num_inputs - num_trues

    if num_trues == 0: return False
    if num_falses == 0: return True

    if not split_candidates:
        return num_trues >= num_falses
    
    best_attribute = min(split_candidates, key=partial(partition_entropy_by, inputs))

    partitions = partition_by(inputs, best_attribute)
    new_candidates = [
        attribute 
        for attribute 
        in split_candidates 
        if attribute != best_attribute
    ]

    subtrees = {
        attribute_value : build_tree_id3(subset, new_candidates)
        for attribute_value, subset
        in partitions.items()
    }

    subtrees[None] = num_trues > num_falses
    return (best_attribute, subtrees)

my_tree = build_tree_id3(inputs)
# print('my_tree = (%s, %s)' % my_tree)