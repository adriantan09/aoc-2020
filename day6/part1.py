import functools

def count_anyone_yes(responses):
    # count the number of unique responses for each response
    responses = list(map(lambda r: len(''.join(set(r))), responses))
    # sum the responses
    return functools.reduce(lambda a, b: a + b, responses)