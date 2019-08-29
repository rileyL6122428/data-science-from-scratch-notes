def shortest_paths_from(from_user):

    shortest_paths_to = { from_user['id']: [[]] }

    frontier = deque(
        (from_user, friend)
        for friend
        in from_user['friends']
    )

    while frontier:

        prev_user, user = frontier.popleft()
        user_id = user['id']

        paths_to_prev_user = shortest_paths_to[prev_user['id']]
        new_paths_to_user = [
            path + [user_id]
            for path
            in paths_to_prev_user
        ]

        old_paths_to_user = shortest_paths_to.get(user_id, [])

        if old_paths_to_user:
            min_path_length = len(old_paths_to_user[0])
        else:
            min_path_length = float('inf')
        
        filtered_new_paths_to_user = [
            path
            for path in new_paths_to_user
            if len(path) <= min_path_length
            and path not in old_paths_to_user
        ]

        shortest_paths_to[user_id] = old_paths_to_user + filtered_new_paths_to_user

        frontier.extend(
            (user, friend)
            for friend in user['friends']
            if friend['id'] not in shortest_paths_to
        )
        
    return shortest_paths_to