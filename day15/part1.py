def function1(spoken):
    for i in range(len(spoken), 2020):
        last_spoken = spoken[i - 1]
        if last_spoken in spoken[:-1]:
            last_found = [i for i, e in enumerate(spoken) if e == last_spoken][-1]
            before_last_found = [i for i, e in enumerate(spoken[:last_found]) if e == last_spoken][-1]
            spoken.append(last_found + 1 - (before_last_found + 1))
        else:
            spoken.append(0)

    return spoken[-1]