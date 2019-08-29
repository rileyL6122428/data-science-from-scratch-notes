import math
import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises'
)
from my_list_vectors import dot_product
import pdb

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def neuron_output(weights, inputs):
    return sigmoid(dot_product(weights, inputs))

def feed_forward(neural_network, input_vector):
    outputs = []

    for layer in neural_network:
        input_with_bias = input_vector + [ 1 ]
        output = [
            neuron_output(neuron, input_with_bias)
            for neuron
            in layer
        ]

        outputs.append(output)
        input_vector = output
    
    return outputs

xor_network = [
    # hidden layer
    [
        [ 20, 20, -30 ], # 'and' neuron
        [ 20, 20, -10 ], # 'or' neuron
    ],

    # output layer
    [
        [ -60, 60, -30 ] # fire on 'or' but not 'and' neuron
    ]
]

# for x in [ 0, 1 ]:
#     for y in [ 0, 1 ]:
#         print(x, y, feed_forward(xor_network, [x, y])[-1])
