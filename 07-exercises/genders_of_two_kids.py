import random

# gather evidence for 1/3 change that both kids girls given at least one
# kid is a girl
def random_kid():
    return random.choice(['BOY', 'GIRL'])

both_girls_count = 0
either_girl_count = 0

for _ in range(10000):
    older = random_kid()
    younger = random_kid()
    if older is 'GIRL' and younger is 'GIRL':
        both_girls_count += 1
    if older is 'GIRL' or younger is 'GIRL':
        either_girl_count += 1

print('from 10000 families')
print('both_girls = %s' % both_girls_count)
print('either_girl = %s' % either_girl_count)
print('both_girls | either_girl = %s' % (both_girls_count / either_girl_count))
