from collections import defaultdict

class MySet:
    def __init__(self, values=None):
        self.dict = defaultdict(lambda: False)
        if values is not None:
            for value in values:
                self.add(value)
    
    def __repr__(self):
        return 'Set = %s' % [key for key in self.dict.keys()]
    
    def add(self, value):
        self.dict[value] = True
    
    def contains(self, value):
        return self.dict[value]
    
    def remove(self, value):
        del self.dict[value]

myTestSet = MySet([1, 2, 3])
print(myTestSet)
print('myTestSet.contains(1) = %s' % myTestSet.contains(1))
print('myTestSet.contains(4) = %s' % myTestSet.contains(4))

print('remove 2 from myTestSet')
myTestSet.remove(2)
print('myTestSet.contains(2) = %s' % myTestSet.contains(2))
print('myTestSet.contains(1) = %s' % myTestSet.contains(1))
                
