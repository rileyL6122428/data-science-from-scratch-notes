import sys
sys.path.append(
    '/Users/rileylittlefield/Desktop/notes/readingnotes/python-ml/data-science-from-scratch/05-exercises'
)
from my_list_vectors import dot_product
from interests import user_interests
from collections import Counter
import math
from collections import defaultdict

popular_interests = Counter(
    interest
    for user in user_interests
    for interest in user
)

def most_popular_new_interests(user_interests, max_results=5):
    suggestions = [
        (interest, frequency)
        for interest, frequency
        in popular_interests.most_common()
        if interest not in user_interests
    ]

    return suggestions[:max_results]

def cosine_similarity(v, w):
    return (
        dot_product(v, w) 
        /
        math.sqrt(dot_product(v, v) * dot_product(w, w))
    )     

unique_interests = sorted(list({
    interest
    for user in user_interests
    for interest in user
}))

def make_user_interest_vector(user_interests):
    return [
        1 if interest in user_interests else 0
        for interest
        in unique_interests
    ]

user_interest_matrix = list(map(make_user_interest_vector, user_interests))

user_similarities = [
    [
        cosine_similarity(interest_vector_i, interest_vector_j)
        for interest_vector_j
        in user_interest_matrix
    ]

    for interest_vector_i
    in user_interest_matrix
]

def most_similar_users_to(user_id):
    pairs = [
        (other_user_id, similarity)
        for other_user_id, similarity
        in enumerate(user_similarities[user_id])
        if user_id != other_user_id and similarity > 0
    ]

    return sorted(
        pairs,
        key=lambda id_similarity: id_similarity[1],
        reverse=True
    )

def user_based_suggestions(user_id, include_current_interests=False):
    suggestions = defaultdict(float)
    for other_user_id, similarity in most_similar_users_to(user_id):
        for interest in user_interests[other_user_id]:
            suggestions[interest] += similarity
    
    suggestions = sorted(
        suggestions.items(),
        key=lambda suggestion_weight: suggestion_weight[1],
        reverse=True
    )

    if include_current_interests:
        return suggestions
    else:
        return [
            (suggestion, weight)
            for suggestion, weight
            in suggestions
            if suggestion not in user_interests[user_id]
        ]

# print(user_based_suggestions(0))