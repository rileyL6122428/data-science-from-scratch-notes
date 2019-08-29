from code_mistakes import mistakes_per_day
from collections import Counter
import math

def quantile(nums, decimal):
    sorted_nums = sorted(nums)
    quantile_index = math.floor(decimal * len(nums))
    return sorted_nums[quantile_index]

def mode(nums):
    return Counter(nums).most_common(1)
    
# print('mistakes_per_day: %s' % mistakes_per_day)
# print('20 percent quantile: %f' % (quantile(mistakes_per_day.values(), .20)))
# print('80 percent quantile: %f' % (quantile(mistakes_per_day.values(), .70)))
# print('most common (mode): %s' % mode(mistakes_per_day.values()))
            
