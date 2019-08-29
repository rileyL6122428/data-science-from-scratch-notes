from k_means import KMeans, squared_distance
from matplotlib import pyplot
from meetup_data import attendees_locations_tuples

def squared_clustering_errors(inputs, k):
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = map(clusterer.classify, inputs)

    return sum(
        squared_distance(input, means[cluster])
        for input, cluster
        in zip(inputs, assignments)
    )

ks = range(1, len(attendees_locations_tuples) + 1)
errors = [
    squared_clustering_errors(attendees_locations_tuples, k)
    for k
    in ks
]

pyplot.plot(ks, errors)
pyplot.xticks(ks)
pyplot.xlabel("k")
pyplot.ylabel("total squared error")
pyplot.title("Total Error vs. # of Clusters")
pyplot.show()