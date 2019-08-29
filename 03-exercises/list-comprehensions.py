# Basic List comprehensions
even_numbers = [ num * 2 for num in range(6) ]
print('event_numbers = %s' % even_numbers)

squares = [ num ** 2 for num in range(6) ]
print('squares = %s' % squares)

# Basic Dict Comprehensions
even_number_mapping = { num : num * 2 for num in range(6) }
print('even_number_mapping = %s' % even_number_mapping)

square_mapping = { root : root ** 2 for root in range(6) }
print('square mapping = %s' % square_mapping)

# multiple loop comprehensions
some_coords = [
    (x, y)
    for x in range(2)
    for y in range(2) # x is accessible in this loop
]

print('some_coords = %s' % some_coords)