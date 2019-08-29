class Table:

    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.rows = []    
    
    def __repr__(self):
        return (
            self.name + ' TABLE' + '\n' +
            str(self.columns) + '\n' + 
            '\n'.join(map(str, self.rows))
        )
    
    def insert(self, row_values):
        if len(row_values) != len(self.columns):
            raise TypeError('wrong number of elements')
        row_dict = dict(zip(self.columns, row_values))
        self.rows.append(row_dict)

    def update(self, updates, predicate):
        for row in self.rows:
            if predicate(row):
                for column, new_value


# EXAMPLE USERS TABLE
users = Table('USERS', ['user_id', 'name', 'num_friends'])
users.insert([0, 'Hero', 0])
users.insert([1, 'Dunn', 2])
users.insert([2, 'Sue', 3])
