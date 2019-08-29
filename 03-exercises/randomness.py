import random

four_uniform_randoms = [ random.random() for _ in range(4) ]
print('four_uniform_randoms = %s' % four_uniform_randoms)

# random includes shuffling utils
up_to_ten = [ number for number in range(10) ]
random.shuffle(up_to_ten)
print('0 - 9 shuffled: %s' % up_to_ten)

# reproducible results can be obtained through seeding
random.seed(10)
print('random.random after seed(10) = %s' % (random.random()))
random.seed(10)
print('random.random after seed(10) = %s' % (random.random()))

