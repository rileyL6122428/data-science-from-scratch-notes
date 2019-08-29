from collections import defaultdict

document = ['sup', 'people', 'how', 'are', 'my', 'people', 'today']

word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1
print(word_counts)

dd_pairs = defaultdict(lambda: [0, 0])
dd_pairs[0][1] = 1
print(dd_pairs)
