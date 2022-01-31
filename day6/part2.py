
def count_everyone_yes(responses):
    total = 0
    for response in responses:
        min_length = len(min(response, key=len))
        print(response)
        for i in range(min_length):
            new_letter = response[0][i]
            print('new letter: ', new_letter)
            same = 0
            for r in response:
                if (same == len(response)):
                    print('SAME', r[i])
                    total += 1
                if (r[i] == new_letter):
                    same += 1
                print(r[i], 'length: ',len(r))
    return total