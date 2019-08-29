# When you want to iterate over a list with indices, using the 
# enumerate function is pythonic

words = [ 'hey', 'ho', 'sup', 'yo' ]
print('here are some words = %s' % words)
for index, word in enumerate(words):
    print('the word %s is at index %s' % (word, index))