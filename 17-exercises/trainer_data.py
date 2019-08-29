trainers = [
    { 'party_average_level': 40, 'team_count': 5, 'beat_game': 0 },
    { 'party_average_level': 77, 'team_count': 1, 'beat_game': 0 },
    { 'party_average_level': 77, 'team_count': 4, 'beat_game': 1 },
    { 'party_average_level': 79, 'team_count': 6, 'beat_game': 1 },
    { 'party_average_level': 65, 'team_count': 5, 'beat_game': 1 },
    { 'party_average_level': 6, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 6, 'team_count': 3, 'beat_game': 0 },
    { 'party_average_level': 20, 'team_count': 2, 'beat_game': 0 },
    { 'party_average_level': 43, 'team_count': 5, 'beat_game': 1 },
    { 'party_average_level': 43, 'team_count': 6, 'beat_game': 1 },
    { 'party_average_level': 58, 'team_count': 4, 'beat_game': 1 },
    { 'party_average_level': 56, 'team_count': 5, 'beat_game': 1 },
    { 'party_average_level': 45, 'team_count': 3, 'beat_game': 0 },
    { 'party_average_level': 100, 'team_count': 5, 'beat_game': 1 },
    { 'party_average_level': 100, 'team_count': 1, 'beat_game': 0 },
    { 'party_average_level': 100, 'team_count': 3, 'beat_game': 1 },
    { 'party_average_level': 95, 'team_count': 3, 'beat_game': 1 },
    { 'party_average_level': 80, 'team_count': 1, 'beat_game': 0 },
    { 'party_average_level': 90, 'team_count': 4, 'beat_game': 1 },
    { 'party_average_level': 22, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 26, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 32, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 5, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 7, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 33, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 40, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 12, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 13, 'team_count': 6, 'beat_game': 0 },
    { 'party_average_level': 18, 'team_count': 2, 'beat_game': 0 },
    { 'party_average_level': 18, 'team_count': 5, 'beat_game': 0 },
    { 'party_average_level': 50, 'team_count': 6, 'beat_game': 1 },
    { 'party_average_level': 60, 'team_count': 5, 'beat_game': 1 },
    { 'party_average_level': 43, 'team_count': 2, 'beat_game': 0 },
    { 'party_average_level': 53, 'team_count': 5, 'beat_game': 1 },
    { 'party_average_level': 52, 'team_count': 5, 'beat_game': 1 },
    { 'party_average_level': 25, 'team_count': 2, 'beat_game': 0 },
    { 'party_average_level': 25, 'team_count': 2, 'beat_game': 0 },
    { 'party_average_level': 20, 'team_count': 3, 'beat_game': 0 },
    { 'party_average_level': 90, 'team_count': 3, 'beat_game': 1 },
    { 'party_average_level': 89, 'team_count': 2, 'beat_game': 0 },
    { 'party_average_level': 100, 'team_count': 2, 'beat_game': 1 },
]

trainer_stats = [
    [ 1, trainer['party_average_level'], trainer['team_count'] ]
    for trainer
    in trainers
]

trainer_avg_levels = [
    trainer['party_average_level']
    for trainer
    in trainers
]

trainer_team_counts = [
    trainer['team_count']
    for trainer
    in trainers
]

beat_game_stats = [
    trainer['beat_game'] for trainer in trainers
]

beat_game_trainers = [
    trainer
    for trainer
    in trainers
    if trainer['beat_game'] == 1
]

not_beat_game_trainers = [
    trainer
    for trainer
    in trainers
    if trainer['beat_game'] == 0
]