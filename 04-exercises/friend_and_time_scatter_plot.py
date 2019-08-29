from matplotlib import pyplot

friend_counts = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes_spent = [175, 170, 205, 120, 220, 130, 105, 145, 190]
participant_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

pyplot.scatter(friend_counts, minutes_spent)

for friend_count, minutes_spent, label in zip(friend_counts, minutes_spent, participant_labels):
    pyplot.annotate(
        label,
        xy=(friend_count, minutes_spent),
        xytext=(5, -5),
        textcoords='offset points'
    )

pyplot.title('Daily Minutes vs Number of Friends')
pyplot.xlabel('# of friends')
pyplot.ylabel('daily minutes spent on the site')
pyplot.show()