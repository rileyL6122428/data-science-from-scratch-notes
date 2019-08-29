from collections import defaultdict

import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/14-exercies'
)
from naive_bayes import tokenize

def word_count_mapper(document):
    for word in tokenize(document):
        yield (word, 1)

def word_count_reducer(word, counts):
    yield (word, sum(counts))

def word_count(documents):
    collector = defaultdict(list)

    for document in documents:
        for word, count in word_count_mapper(document):
            collector[word].append(count)
    
    return [
        output
        for word, counts in collector.items()
        for output in word_count_reducer
    ]
