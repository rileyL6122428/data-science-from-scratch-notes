from code_mistakes import mistakes_per_day
from central_tendencies import mean
from functools import reduce
from quantile import quantile
import math

def value_range(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[len(nums) - 1] - sorted_nums[0]

def mean_deviations(nums):
    nums_mean = mean(nums)
    return [
        num - nums_mean for num in nums
    ]

def sum_of_squares(nums):
    return reduce(lambda cumulative, next: cumulative + next ** 2, nums, 0)

def variance(nums):
    deviations = mean_deviations(nums)
    return sum_of_squares(deviations) / (len(nums) - 1)

def standard_deviation(nums):
    return math.sqrt(variance(nums))

def interquartile_range(nums):
    return quantile(nums, 0.75) - quantile(nums, 0.25)

# print('mistakes per day: %s' % mistakes_per_day)
# print('value_range: %s' % value_range(mistakes_per_day.values()))
# print('mean_deviations: %s' % mean_deviations(mistakes_per_day.values()))
# print('variance: %s' % variance(mistakes_per_day.values()))
# print('standard deviation: %s' % standard_deviation(mistakes_per_day.values()))
# print('interquartile range: %s' % interquartile_range(mistakes_per_day.values()))
