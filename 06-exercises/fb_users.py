class User:
    def __init__(self, **kwargs):
        self.num_friends = kwargs.get('num_friends')
        self.avg_time = kwargs.get('avg_time')
    
    def __repr__(self):
        return 'User: num_friends=%s & avg_time=%s' % (self.num_friends, self.avg_time)

users = [
    User(num_friends=3, avg_time=5),
    User(num_friends=9, avg_time=8),
    User(num_friends=3, avg_time=4),
    User(num_friends=3, avg_time=7),
    User(num_friends=2, avg_time=4),
    User(num_friends=1, avg_time=2),
]

# print(users[0].num_friends);
