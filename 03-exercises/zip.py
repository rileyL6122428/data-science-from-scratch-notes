my_nums = [1, 2, 3]
my_letters = ['a', 'b', 'c']

my_zip = list(zip(my_nums, my_letters))
print('my_zip = %s' % my_zip)

# can be unpacked with a neat trick
unpacked_nums, unpacked_letters = zip(*my_zip)
print('unpacked_nums', unpacked_nums)
print('unpacked_letters', unpacked_letters)
