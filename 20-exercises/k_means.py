from functools import reduce
import random

def vector_sum(vectors):
    summed_vector = []
    for component_index in range(len(vectors[0])):
        summed_vector.append(0)

        for vector in vectors:
            summed_vector[component_index] += vector[component_index]
    
    return summed_vector

def scalar_multiply(scalar, vector):
    return [
        scalar * component
        for component
        in vector
    ]

def vector_mean(vectors):
    component_count = len(vectors)
    return scalar_multiply(1 / component_count, vector_sum(vectors))

def squared_distance(vector_a, vector_b):
    squared_component_differences = [
        (component_a - component_b) ** 2
        for component_a, component_b
        in zip(vector_a, vector_b)
    ]

    return reduce(lambda num_a, num_b: num_a + num_b, squared_component_differences, 0)

class KMeans:

    def __init__(self, number_of_clusters):
        self.number_of_clusters = number_of_clusters
        self.means = None
    
    def classify(self, input):
        return min(
            range(self.number_of_clusters),
            key=lambda index: squared_distance(input, self.means[index])
        )
    
    def train(self, inputs):
        self.means = random.sample(inputs, self.number_of_clusters)
        assignments = None

        while True:
            print('classifier means: %s' % self.means)
            new_assignments = list(map(self.classify, inputs))
            if assignments == new_assignments:
                return
            else:
                assignments = new_assignments
                for cluster_index in range(self.number_of_clusters):
                    clutsered_inputs = [
                        input
                        for input, assignment
                        in zip(inputs, assignments)
                        if assignment == cluster_index
                    ]
                    if clutsered_inputs:
                        self.means[cluster_index] = vector_mean(clutsered_inputs)
# on page 319