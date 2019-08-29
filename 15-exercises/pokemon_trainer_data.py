trainers = [
    { 'pokemon_count': 2, 'battle_win_count': 4 },
    { 'pokemon_count': 1, 'battle_win_count': 3 },
    { 'pokemon_count': 1, 'battle_win_count': 0 },
    { 'pokemon_count': 5, 'battle_win_count': 9 },
    { 'pokemon_count': 5, 'battle_win_count': 6 },
    { 'pokemon_count': 4, 'battle_win_count': 4 },
]

trainer_pokemon_counts = [
    trainer['pokemon_count']
    for trainer
    in trainers
]

trainer_win_counts = [
    trainer['battle_win_count']
    for trainer
    in trainers
]