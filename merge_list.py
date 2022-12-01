
def merge_lists(l1, l2):
    length_l1 = len(l1)
    length_l2 = len(l2)
    new_list = []

    dict = {'l1': 0, 'l2': 0}

    for _ in range(length_l1 + length_l2):
        if dict['l1'] != length_l1 and (dict['l2'] != length_l2 and l1[dict['l1']] < l2[dict['l2']]) or (dict['l1'] != length_l1 and dict['l2'] == length_l2):
            new_list.append(l1[dict['l1']])
            dict['l1'] += 1 if dict['l1'] < length_l1 else 0
        else:
            new_list.append(l2[dict['l2']])
            dict['l2'] += 1 if dict['l2'] < length_l2 else 0

    return new_list
