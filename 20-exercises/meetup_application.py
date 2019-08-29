import random
from k_means import KMeans
from meetup_data import attendees_locations_tuples

random.seed(0)
clusterer = KMeans(3)
clusterer.train(attendees_locations_tuples)
print(clusterer.means)
