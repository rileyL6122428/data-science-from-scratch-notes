from recommenders import user_interests, user_interest_matrix, unique_interests, cosine_similarity
import pdb
# rows are interests, cols are users, hence naming order
interest_user_matrix = [
    [
        user_interest_vector[interest_index]
        for user_interest_vector 
        in user_interest_matrix
    ]

    for interest_index, _
    in enumerate(unique_interests)
]
pdb.set_trace()
interest_similarities = [
    [
        cosine_similarity(interest_vector_i, interest_vector_j)
        for interest_vector_j
        in interest_user_matrix
    ]

    for interest_vector_i
    in interest_user_matrix
]
pdb.set_trace()

big_data_index = 0
hadoop_index = 4
print(cosine_similarity(
    interest_user_matrix[big_data_index],
    interest_user_matrix[hadoop_index]
))

def by_similarity(interest_similarity_tuple):
    _, similarity = interest_similarity_tuple
    return similarity

def most_similar_interests_to(interest_id):
    similarities = interest_similarities[interest_id]
    pairs = [
        (unique_interests[other_interest_id], similarity)
        for other_interest_id, similarity
        in enumerate(similarities)
        if interest_id != other_interest_id and similarity > 0
    ]

    return sorted(
        pairs,
        key=by_similarity,
        reverse=True
    )

print(unique_interests[0])
print(most_similar_interests_to(0))