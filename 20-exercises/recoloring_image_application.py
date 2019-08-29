from k_means import KMeans
from matplotlib import image as mat_image
from matplotlib import pyplot


path_to_png_file = "/Users/rileylittlefield/Desktop/squirtle.png"
squirtle_image = mat_image.imread(path_to_png_file)


squirtle_pixels = [
    pixel
    for row in squirtle_image
    for pixel in row
]

clusterer = KMeans(5)
clusterer.train(squirtle_pixels)

def recolor(pixel):
    cluster = clusterer.classify(pixel)
    return clusterer.means[cluster]

new_squirtle_image = [
    [ 
        recolor(pixel) 
        for pixel 
        in row 
    ]
    for row in squirtle_image
]

pyplot.imshow(new_squirtle_image)
pyplot.axis('off')
pyplot.show()
