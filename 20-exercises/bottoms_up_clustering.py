from meetup_data import attendees_locations_tuples
from matplotlib import pyplot
from k_means import vector_mean

def distance(vector_a, vector_b):
    sum_of_squared_component_diffs = sum([
        (component_a - component_b) ** 2
        for component_a, component_b
        in zip(vector_a, vector_b)
    ])
    return sum_of_squared_component_diffs ** (1/2)


# represent leaves as single tuples
# non-leaf nodes are represented as (merge_order, leaf_list)

def is_leaf(cluster):
    return len(cluster) == 1

def get_children(cluster):
    if is_leaf(cluster):
        raise TypeError('a leaf cluster has no children')
    else:
        return cluster[1]
    
def get_values(cluster):
    if is_leaf(cluster):
        return cluster
    else:
        return [
            value
            for child in get_children(cluster)
            for value in get_values(child)
        ]

def cluster_distance(cluster1, cluster2, distance_agg=max):
    return distance_agg([
        distance(input_1, input_2)
        for input_1 in get_values(cluster1)
        for input_2 in get_values(cluster2)
    ])

def get_merge_order(cluster):
    if is_leaf(cluster):
        return float('inf')
    else:
        return cluster[0]

def bottom_up_cluster(inputs, distance_agg=max):
    clusters = [ (input,) for input in inputs ]

    while len(clusters) > 1:
        cluster_1, cluster_2 = min(
            [
                (cluster_1, cluster_2)
                for index_1, cluster_1 in enumerate(clusters) 
                for cluster_2 in clusters[:index_1]
            ],

            key=
            lambda cluster_pair: cluster_distance(cluster_pair[0], cluster_pair[1], distance_agg)
        )

        clusters = [
            cluster
            for cluster in clusters
            if cluster != cluster_1 and cluster != cluster_2
        ]

        merged_cluster = (len(clusters), [cluster_1, cluster_2])

        clusters.append(merged_cluster)

    return clusters[0]

def generate_clusters(base_cluster, num_clusters):
    clusters = [ base_cluster ]

    while len(clusters) < num_clusters:
        next_cluster = min(clusters, key=get_merge_order)
        clusters = [
            cluster 
            for cluster in clusters
            if cluster != next_cluster
        ]
        clusters.extend(get_children(next_cluster))
    
    return clusters


base_cluster = bottom_up_cluster(attendees_locations_tuples)
# print(base_cluster)

three_clusters = [
    get_values(cluster)
    for cluster
    in generate_clusters(base_cluster, 3)
]

print('three clusters = %s' % three_clusters)

plot_zip_parameters = zip(
    [1, 2, 3],
    three_clusters,
    ['D', 'o', '*'],
    ['r', 'g', 'b'],
)

for index, cluster, marker, color in plot_zip_parameters:
    xs, ys = zip(*cluster)
    pyplot.scatter(xs, ys, color=color, marker=marker)
    x, y = vector_mean(cluster)
    pyplot.plot(x, y, marker='$' + str(index) + '$', color='black')

pyplot.title('User Locations-3 Bottom-Up Clusters, Min')
pyplot.xlabel('blocks East of city center')
pyplot.ylabel('blocks North of city center')
pyplot.show()
