from matplotlib import pyplot
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

pyplot.bar(
    [grade_decile for grade_decile in histogram.keys()],
    histogram.values(),
    8 # historgram width
)

pyplot.axis([-5, 105, 0, 5])

pyplot.xticks([10 * num for num in range(11)])
pyplot.xlabel('decile')
pyplot.ylabel('# of students')
pyplot.title('Distribution of exam 1 grades')
pyplot.show()