def farness(user):
    return sum(
        len(paths[0])
        for paths
        in user['shortest_paths'].values()
    )

for user in users:
    user['closeness_centrality'] = 1 / farness(user)