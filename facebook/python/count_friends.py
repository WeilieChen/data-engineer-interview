def solution(data):
    counts = {}

    for friend_group in data:
        if len(friend_group) == 1:
            counts[friend_group[0]] = 0
        else:
            for person in friend_group:
                counts[person] = counts.get(person, 0) + 1

    return counts

assert count_friends([[2,3],[3,4],[5]]) == {2: 1, 3: 2, 4: 1, 5: 0}