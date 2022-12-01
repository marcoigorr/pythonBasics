
def merge_lists(l1, l2):
    length_l1 = len(l1)
    length_l2 = len(l2)
    new_list = []

    count_l1 = 0
    count_l2 = 0

    # Debug
    for _ in range(length_l1 + length_l2):
        if count_l1 != length_l1 and (count_l2 != length_l2 and l1[count_l1] < l2[count_l2]) or (count_l1 != length_l1 and count_l2 == length_l2):
            new_list.append(l1[count_l1])
            count_l1 += 1 if count_l1 < length_l1 else 0
        else:
            new_list.append(l2[count_l2])
            count_l2 += 1 if count_l2 < length_l2 else 0

    return new_list
