
def count_everyone_yes(groups):
    total = 0
    for group in groups:
        answer = set(group[0])
        for person in group:
            answer = answer & set(person)
        total += len(answer)
    return total