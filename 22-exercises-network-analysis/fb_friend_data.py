users = [
    { 'id': 0, 'name': 'Hero' },
    { 'id': 1, 'name': 'Dunn' },
    { 'id': 2, 'name': 'Sue' },
    { 'id': 3, 'name': 'Chi' },
    { 'id': 4, 'name': 'Thor' },
    { 'id': 5, 'name': 'Clive' },
    { 'id': 6, 'name': 'Hicks' },
    { 'id': 7, 'name': 'Devin' },
    { 'id': 8, 'name': 'Kate' },
    { 'id': 9, 'name': 'Klein' },
]

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

for user in users:
    user['friends'] = []

for i, j in friendships:
    users[i]['friends'].append(users[j])
    users[j]['friends'].append(users[i])

endorsements = [
    (0, 1),
    (1, 0),
    (0, 2),
    (2, 0),
    (1, 2),
    (2, 1),
    (1, 3),
    (2, 3),
    (3, 4),
    (5, 4),
    (5, 6),
    (7, 5),
    (6, 8),
    (8, 7),
    (8, 9)
]

for user in users:
    user['endorses'] = []
    user['endorsed_by'] = []

for source_id, target_id in endorsements:
    users[source_id]['endorses'].append(users[target_id])
    users[target_id]['endorsed_by'].append(users[source_id])


