import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/07-exercises'
)
from prob import invert_normal_cdf
import random, math
from collections import Counter
from matplotlib import pyplot

# One dimensional data sets

# uniform between -100 & 100
uniform = [ 200 * random.random() - 100 for _ in range(100000) ]

# normal with mean 0 and std_dev 57
normal = [
    invert_normal_cdf(random.random()) * 57
    for _
    in range(100000)
]

def bucketize(point, bucket_size):
    return math.floor(point/bucket_size) * bucket_size

# BUCKETS THE POINTS AND COUNTS HOW MANY BUCKETS
def make_histogram(points, bucket_size):
   return Counter(bucketize(point, bucket_size) for point in points);

def plot_histogram(points, bucket_size, title=""):
    counter = make_histogram(points, bucket_size)
    x_vals, y_vals = zip(*[
        (bucket, counter.get(bucket)) 
        for bucket
        in counter.keys()
    ])
    pyplot.bar(x_vals, y_vals, width=bucket_size, label=title)
    pyplot.show()

# plot_histogram(uniform, 5, "uniform between -100 to 100")
# plot_histogram(normal, 20, "uniform between -100 to 100")
