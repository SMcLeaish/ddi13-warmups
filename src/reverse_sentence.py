def reverse_list(sen: str) -> str:
    return ' '.join(reversed(sen.split()))


def reverse_iter(sen: str) -> str:
    lst = sen.split()
    rev_lst = []
    while lst:
        rev_lst.append(lst.pop())
    return ' '.join(rev_lst)


sentence = 'I am going to the store'
print(reverse_list(sentence))
print(reverse_iter(sentence))
