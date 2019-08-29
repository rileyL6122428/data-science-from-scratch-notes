import random
from collections import Counter
import random

def sample_from(weights):
    weights_sum = sum(weights)
    random_weight_fraction = weights_sum * random.random()
    for index, weight in enumerate(weights):
        random_weight_fraction -= weight
        if random_weight_fraction <= 0:
            return index

documents = [
    ['Hadoop', 'Big Data', 'HBase', 'Java', 'Spark', 'Storm', 'Cassandra'],
    ['NoSql', 'MongoDB', 'Cassandra', 'HBase', 'Postgres'],
    ['Python', 'scikit-learn', 'scipy', 'numpy', 'statsmodels', 'pandas'],
    ['R', 'Python', 'statistics', 'regression', 'probability'],
    ['machine learning', 'regression', 'decision trees', 'libsvm'],
    ['Python', 'R', 'Java', 'C++', 'Haskell', 'programming languages'],
    ['statistics', 'probability', 'mathematics', 'theory'],
    ['machine learning', 'scikit-learn', 'Mahout', 'neural networks'],
    ['neural networks', 'deep learning', 'Big Data', 'artificial intelligence'],
    ['Hadoop', 'Java', 'MapReduce', 'Big Data'],
    ['statistics', 'R', 'statsmodels'],
    ['C++', 'deep learning', 'artificial intelligence', 'probability'],
    ['pandas', 'R', 'Python'],
    ['databases', 'HBase', 'Postgres', 'MySQL', 'MongoDB'],
    ['libsvm', 'regression', 'support vector machines']
]


document_topic_counts = [
    Counter() for _ in documents    
]

topic_total_k = 4

topic_word_counts = [
    Counter() for _ in range(topic_total_k)
]

topic_counts = [
    0 for _ in range(topic_total_k)
]

document_lengths = list(map(len, documents))

distinct_words = set(
    word 
    for document in documents 
    for word in document
)
distinct_words_count = len(distinct_words)

document_count_D = len(documents)

def prob_topic_given_document(topic, doc_index, smoothing_addend=0.01):
    return (
        (document_topic_counts[doc_index][topic] + smoothing_addend) 
        /
        (document_lengths[doc_index] + topic_total_k * smoothing_addend)
    )

def prob_word_given_topic(word, topic, smoothing_addend=0.01):
    return (
        (topic_word_counts[topic][word] + smoothing_addend)
        /
        (topic_counts[topic] + distinct_words_count * smoothing_addend)
    )

def topic_weight(doc_index, word, topic):
    return prob_word_given_topic(word, topic) * prob_topic_given_document(topic, doc_index)

def choose_new_topic(doc_index, word):
    return sample_from([
        topic_weight(doc_index, word, topic)
        for topic
        in range(topic_total_k)
    ])

random.seed(0)
document_topics = [
    [ random.randrange(topic_total_k) for word in document ]
    for document
    in documents
]

for doc_index in range(document_count_D):
    for word, topic in zip(documents[doc_index], document_topics[doc_index]):
        document_topic_counts[doc_index][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1

for iter in range(1000):
    for doc_index in range(document_count_D):
        for word_index, (word, topic) in enumerate(zip(documents[doc_index], document_topics[doc_index])):

            # remove this word / topic from the counts
            # so that it doesn't influence the weights
            document_topic_counts[doc_index][topic] -= 1
            topic_word_counts[topic][word] -= 1
            topic_counts[topic] -= 1
            document_lengths[doc_index] -= 1

            new_topic = choose_new_topic(doc_index, word)
            document_topics[doc_index][word_index] = new_topic

            # and now add it back to the counts
            document_topic_counts[doc_index][new_topic] += 1
            topic_word_counts[new_topic][word] += 1
            topic_counts[new_topic] += 1
            document_lengths[doc_index] += 1


# Examine 5 heavist weighted words
# for topic_index, word_counts in enumerate(topic_word_counts):
#     print('')
#     for word, count in word_counts.most_common():
#         if count > 0: 
#             print(topic_index, word, count)