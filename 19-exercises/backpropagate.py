from feed_forward_net import feed_forward
import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises'
)
from my_list_vectors import dot_product
import pdb

def backpropagate(network, input_vector, targets):
    # pdb.set_trace()
    hidden_layer, output_layer = network[0], network[1]
    hidden_outputs, outputs = feed_forward(network, input_vector)

    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [
        output * ( 1 - output ) * ( output - target ) # error gradient as func of weights
        for output, target
        in zip(outputs, targets)
    ]

    # adjust weights for output layer, one neuron at a time
    for i, output_neuron_weight in enumerate(output_layer):
        for j, hidden_output_weight in enumerate(hidden_outputs + [ 1 ]):
            output_neuron_weight[j] -= output_deltas[i] * hidden_output_weight
    
    # backpropagate errors to hidden layer
    hidden_deltas = [
        hidden_output * 
        (1 - hidden_output) * 
        dot_product(output_deltas, [ neuron[i] for neuron in output_layer ])

        for i, hidden_output
        in enumerate(hidden_outputs)
    ]

    # adjust weights for hidden layer, one neuron at a time
    for i, hidden_neuron in enumerate(hidden_layer):
        for j, input in enumerate(input_vector + [ 1 ]):
            hidden_neuron[j] -= hidden_deltas[i] * input
    
    # DOUBLE CHECK ABOVE CODE AGAINST BOOK