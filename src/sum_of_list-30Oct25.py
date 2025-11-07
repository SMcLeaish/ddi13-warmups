def pos_neg_sum(lst: list[int]) -> tuple[int, int]:
    pos = [x for x in lst if x > 0]
    neg = [x for x in lst if x < 0]
    return (sum(pos), sum(neg))


def pos_neg_for(lst: list[int]) -> tuple[int, int]:
    pos = 0
    neg = 0
    for num in lst:
        if num < 0:
            neg += num
        else:
            pos += num
    return (pos, neg)


lst = [2, 20, -40, 23, -2, -4, -5, 30, 1, 2, 1, 10, -1]
print(pos_neg_sum(lst))
print(pos_neg_for(lst))
