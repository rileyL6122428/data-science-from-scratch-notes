from fb_users import users
from functools import reduce
from dispersion import mean_deviations, standard_deviation

friend_counts = [
    user.num_friends for user in users
]

avg_times_on_site = [
    user.avg_time for user in users
]

def dot(vector_a, vector_b):
    vector_zip = zip(vector_a, vector_b)
    coord_products = map(lambda coords: coords[0] * coords[1], vector_zip)
    return reduce(lambda x, y: x + y, coord_products)

# measure how two variables change in tandem from their means
# is the sum of mean dev products over n - 1
# when both coords in coord pairs are same sign, positive numbers enter sum
# when signs differ, negative nums enter sum
# if covariance is large, x & y get large together
# if covariance is large negative, y gets small as x gets big
# if covariance is close to zero, no such relationship exists
# hard to say what counts as an 'absoulte' large variance
def covariance(x, y):
    pair_total = len(x)
    return dot(mean_deviations(x), mean_deviations(y)) / (pair_total - 1)

# correlation is the same as covariance, except standard dev of both vars
# is divided out
# result is in [-1, 1]. -1 represents perfect anti correlation
# result is in [-1, 1]. 1 represents perfect positive correlation
# note that correlation can be very sensitive to outliers
def correlation(x, y):
    standard_dev_x = standard_deviation(x)
    standard_dev_y = standard_deviation(y)
    if(standard_dev_x is 0 or standard_dev_y is 0):
        return 0
    else:
        return covariance(x, y) / (standard_deviation(x) * standard_deviation(y))

# print('users: %s' % users)
# print('friend counts: %s' % friend_counts)
# print('avg_times_on_site: %s' % avg_times_on_site)
# print('[1, 2] * [2, 4] = %s' % (dot([1, 2], [2, 4])))
# print('covariance(friend_counts, avg_times_on_site) = %s' % covariance(friend_counts, avg_times_on_site))
# print('correlation(friend_counts, avg_times_on_site) = %s' % correlation(friend_counts, avg_times_on_site))
