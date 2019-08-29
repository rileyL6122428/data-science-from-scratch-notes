from code_mistakes import mistakes_per_day
print('avg code mistakes per day: %s' % mistakes_per_day)

# lets calc stats
num_points = len(mistakes_per_day)
print('number of data points: %s' % num_points)

mistake_max = max(mistakes_per_day.values())
print('mistake_max = %s' % mistake_max)

mistake_min = min(mistakes_per_day.values())
print('mistake_min = %s' % mistake_min)