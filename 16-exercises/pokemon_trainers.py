trainers = [
    { 'party_type_count': 3, 'average_level': 24, 'badges': 4 },
    { 'party_type_count': 5, 'average_level': 28, 'badges': 5 },
    { 'party_type_count': 2, 'average_level': 5, 'badges': 0 },
    { 'party_type_count': 1, 'average_level': 15, 'badges': 1 },
    { 'party_type_count': 9, 'average_level': 40, 'badges': 7 },
    { 'party_type_count': 6, 'average_level': 40, 'badges': 6 },
    { 'party_type_count': 1, 'average_level': 30, 'badges': 3 },
    { 'party_type_count': 4, 'average_level': 50, 'badges': 8 },
    { 'party_type_count': 7, 'average_level': 38, 'badges': 5 },
    { 'party_type_count': 1, 'average_level': 10, 'badges': 0 },
    { 'party_type_count': 4, 'average_level': 10, 'badges': 1 },
    { 'party_type_count': 4, 'average_level': 6, 'badges': 1 },
    { 'party_type_count': 10, 'average_level': 3, 'badges': 0 },
    { 'party_type_count': 12, 'average_level': 10, 'badges': 2 },
    { 'party_type_count': 12, 'average_level': 80, 'badges': 8 },
    { 'party_type_count': 9, 'average_level': 50, 'badges': 6 }
]

trainer_party_stats = [
    [ 1, trainer['party_type_count'], trainer['average_level'] ]
    for trainer
    in trainers
]

trainer_badge_counts = [
    trainer['badges']
    for trainer
    in trainers
]
