# None is Python's Null
x = None
print('x == None: %s' % (x == None))
print('x is None: %s' % (x is None))

# falsey vals
if not False:
    print('false is falsey')
if not None:
    print('None is falsey')
if not []:
    print('[] is falsey')
if not {}:
    print('{} is falsey')
if not "":
    print('"" is falsey')
if not set():
    print('set() is falsey')
if not 0:
    print('0 is falsey')
if not 0.0:
    print('0.0 is falsey')

# python also supports short circuiting

xx = "" and "a"
print('xx is "": %s' % (xx is ""))
xx = " " and "a"
print('xx is a: %s' % (xx is "a"))


# python has cool list checkers
xxx = [1, 2, 3]
print('xxx = %s' % xxx)
print('all(xxx) = %s' % (all(xxx)))
print('any(xxx) = %s' % (any(xxx)))

xxx = [0, 1, 2]
print('xxx = %s' % xxx)
print('all(xxx) = %s' % (all(xxx)))
print('any(xxx) = %s' % (any(xxx)))

xxx = [0, 0, 0]
print('xxx = %s' % xxx)
print('all(xxx) = %s' % (all(xxx)))
print('any(xxx) = %s' % (any(xxx)))