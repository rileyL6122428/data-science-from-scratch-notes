from users import users
from friendships import friendships
from interests import interests

for user in users:
    user["friends"] = []

for id1, id2 in friendships:
    users[id1]["friends"].append(users[id2])
    users[id2]["friends"].append(users[id1])

def number_of_friends(user):
    return len(user["friends"])

total_friend_connections = sum(
    number_of_friends(user) for user in users
)
print("total friend connections %s" % total_friend_connections)

friend_connection_average = total_friend_connections / len(users)
print("Average number of friends: %s" % friend_connection_average)

num_friends_by_id = [
    (user["id"], number_of_friends(user)) for user in users
]
print(num_friends_by_id)

friend_count_index = 1
sorted_friend_counts = sorted(
    num_friends_by_id,
    key=lambda friend_by_id_tuple : friend_by_id_tuple[friend_count_index],
    reverse=True
)

print("sorted friend counts by ID: %s" % sorted_friend_counts)

def friends_of_friend_ids_bad(user):
    return [
        friend_of_friend['id']
        for friend in user['friends']
        for friend_of_friend in friend['friends']
    ]

hero = users[0]
print('naive foafs for \'hero\': %s' % friends_of_friend_ids_bad(hero))

from collections import Counter

def not_the_same(user_a, user_b):
    return user_a['id'] != user_b['id']

def not_friends(user, other_user):
    return all(
        not_the_same(friend, other_user) for friend in user['friends']
    )

def friends_of_friend_ids(user):
    return Counter(
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf) and not_friends(user, foaf)
    )

print(friends_of_friend_ids(users[3]))

def data_scientists_who_like(target_interest):
    return [
        user_id
        for user_id, user_interest in interests
        if user_interest == target_interest
    ]