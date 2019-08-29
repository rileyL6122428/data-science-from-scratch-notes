from favorite_language_data import coord_language_pairs
from matplotlib import pyplot
from k_nearest_neighbors import knn_classify

for k in [1, 3, 5, 7]:
    correct_predictions = 0

    for city in coord_language_pairs:
        other_cities = [
            other_city
            for other_city
            in coord_language_pairs
            if other_city != city
        ]

        predicted_language = knn_classify(k, other_cities, city[0])
        actual_language = city[1]
        print(
            'coords, actual_language, predicted_language = %s, %s, %s' % (city[0], actual_language, predicted_language)
        )



plots = {
    "Java": ([], []),
    "Python": ([], []),
    "R": ([], [])
}

markers = { "Java": "o", "Python": "s", "R": "^" }
colors = { "Java": "r", "Python": "b", "R": "g" }

for (latitude, longitude), language in coord_language_pairs:
    plots[language][0].append(latitude)
    plots[language][1].append(longitude)

for language, (x, y) in plots.items():
    pyplot.scatter(
        x, y, 
        color=colors[language], 
        marker=markers[language], 
        label=language,
        zorder=10
    )

pyplot.legend(loc=0)
pyplot.title("Favorite Programming Languages")
pyplot.show()

