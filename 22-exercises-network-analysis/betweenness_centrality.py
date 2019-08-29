from collections import deque
from shortest_paths_from import 

for user in users:
    user['shortest_paths'] = shortest_paths_from(user)

for user in users:
    user['betweenness_centrality'] = 0.0

for source in users:
    source_id = source['id']

    for target_id, paths in source['shortest_paths'].items():
        if source_id < target_id:
            num_paths = len(paths)
            centrality_contribution = 1 / num_paths

            for path in paths:
                for id in path:
                    if id not in [source_id, target_id]:
                        users[id]['betweenness_centrality'] += centrality_contribution


