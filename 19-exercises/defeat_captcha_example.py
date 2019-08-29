import random
from backpropagate import backpropagate
from feed_forward_net import feed_forward
import pdb
from matplotlib import pyplot, patches, cm

inputs = [
    # the number zero
    [ 
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1
    ], 

    # the number one
    [ 
        0, 0, 1, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 1, 0, 0
    ], 

    # the number two
    [ 
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 0,
        1, 1, 1, 1, 1
    ],

    # the number three
    [ 
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        1, 1, 1, 1, 1
    ], 

    # the number four
    [ 
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        0, 0, 0, 0, 1
    ], 

    # the number five
    [ 
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        1, 1, 1, 1, 1
    ], 

    # the number six
    [ 
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1
    ],

    # the number seven
    [ 
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        0, 0, 0, 0, 1,
        0, 0, 0, 0, 1,
        0, 0, 0, 0, 1
    ],

    # the number eight
    [ 
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1
    ],

    # the number nine
    [ 
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 1,
        1, 1, 1, 1, 1
    ],
]

targets = [
    [ 
        1 if output_index == number else 0 
        for output_index 
        in range(10) 
    ]

    for number
    in range(10)
]

random.seed(1)
input_size = 25
num_hidden_neurons = 5
output_size = 10

hidden_layer = [
    [
        random.random() 
        for _ 
        in range(input_size + 1) # + 1 for bias weight
    ]

    for _ in range(num_hidden_neurons)
]

output_layer = [
    [
        random.random() 
        for _ 
        in range(num_hidden_neurons + 1) # + 1 for bias weight
    ]

    for _ in range(output_size)
]

network = [ hidden_layer, output_layer ]

for _ in range(50000):
    for input_vector, target_vector in zip(inputs, targets):
        backpropagate(network, input_vector, target_vector)        

def predict(input):
    return feed_forward(network, input)

# DEBUG THE OUTPUT FROM THIS PRINT STATEMENT
# for number, number_as_vector in enumerate(inputs):
#     prediction = predict(number_as_vector)[1]
#     print('predict my %s: %s \n\n' % (number, prediction))


# TRY TO UNDERSTAND BETTER WHY THIS WORKS! THEN ADD FLASHCARDS!

# PLOT THE WEIGHTS
# for hidden_neuron_index in range(5):

#     weights = network[0][hidden_neuron_index]
#     abs_weights = list(map(abs, weights))

#     grid = [
#         abs_weights[row:( row + 5 )]
#         for row in range(0, 25, 5)
#     ]

#     ax = pyplot.gca()

#     ax.imshow(
#         grid,
#         cmap=cm.binary,
#         interpolation='none'
#     )

#     def patch(x, y, hatch, color):
#         return patches.Rectangle(
#             (x - 0.5, y - 0.5),
#             1,
#             1,
#             hatch=hatch,
#             fill=False,
#             color=color
#         )

#     for i in range(5):
#         for j in range(5):
#             if weights[5 * i + j] < 0:
#                 ax.add_patch(patch(j, i, '/', "white"))
#                 ax.add_patch(patch(j, i, '\\', "black"))

#     pyplot.show()
