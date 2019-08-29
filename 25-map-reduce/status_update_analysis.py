from collections import Counter

"""
    EXAMPLE STATUS UPDATE

    {
        'id': 1,
        'username': 'joelgrus',
        'text': 'Is anyone interested in a data science book?',
        'created_at': datetime.datetime(2013, 12, 21, 11, 47, 0),
        'liked_by': ['data_guy', 'data_gal', 'mike']
    }
"""

def data_science_day_mapper(status_update):
    if "data science" in status_update['text'].lower():
        day_of_week = status_update['created_by'].weekday()
        yield (day_of_week, 1)
    
# FIND THE MOST COMMON WORD A USER PUTS IN THEIR STATUS UPDATE

def words_per_user_mapper(status_update):
    username = status_update['username']
    for word in tokenize(status_update['text']):
        yield (username, (word, 1))

def most_popular_word_reducer(user, words_and_counts):
    word_counts = Counter()
    for word, count in words_and_counts:
        word_counts[word] += count
    
    word, count = word_counts.most_common(1)[0]

    yield (user, (word, count))

# FIND NUMBER OF DISTINCT STATUS-LIKERS FOR EACH USER
def liker_mapper(status_update):
    username = status_update['username']

    for liker in status_update['liked_by']:
        yield (user, liker)

# use count_disctinct_reducer

