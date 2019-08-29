x = [4, 1, 2, 3]
print('x = %s' % x)

y = sorted(x) # creates a new, sorted array
print('after y = sorted(x)')
print('x = %s' % x)
print('y = %s' % y)

x.sort()      # sorts x in place
print('after a.sort()')
print('x = %s' % x)
print('y = %s' % y)
