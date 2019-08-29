from fb_friend_data import users

endorsements_by_id = [
    (user['id'], len(user['endorsed_by']))
    for user
    in users
]

sorted_endorsements_by_id = sorted(
    endorsements_by_id,
    key=lambda id_endoresment_total_tuple: id_endoresment_total_tuple[1],
    reverse=True
)

def page_rank(users, damping=0.85, num_iters=100):
    num_users = len(users)
    pr = { 
        user['id'] : 1 / num_users 
        for user 
        in users 
    }

    base_pr = (1 - damping) / num_users

    for _ in range(num_iters):
        next_pr = { user['id'] : base_pr for user in users }    
        for user in users:
            links_pr = pr[user['id']] * damping
            for endorsee in user['endorses']:
                next_pr[endorsee['id']] += links_pr / len(user['endorses'])
        pr = next_pr
    
    return pr

print(page_rank(users))
