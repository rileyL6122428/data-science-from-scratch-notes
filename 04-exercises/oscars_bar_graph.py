from matplotlib import pyplot

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Ghandi', 'West Side Story']
oscar_counts = [5, 11, 3, 8, 10]
x_coords = [ index for index, _ in enumerate(movies)]

pyplot.bar(x_coords, oscar_counts)

pyplot.ylabel('# of academy awards')
pyplot.title('My Favorite Movies')

pyplot.xticks([index for index, _ in enumerate(movies)], movies)
pyplot.show()