from collections import Counter

number_counts = Counter([0, 1, 2, 0])
print(number_counts)

document = ['hello', 'world', 'hello', 'goodbye', 'moon']
word_counts = Counter(document)
print(word_counts)

print('most common word in documnet: %s' % word_counts.most_common(1))