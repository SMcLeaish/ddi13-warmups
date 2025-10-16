from collections import Counter
from functools import reduce


def clean_sentence(sen: str) -> list[str]:
    return sen.replace('.', '').split()


def word_count(word_list: list[str]) -> dict[str, int]:
    return {word: word_list.count(word) for word in set(word_list)}


def word_reduce(word_list: list[str]) -> dict[str, int]:
    return reduce(
        lambda d, word: d.update({word: d.get(word, 0) + 1}) or d,
        word_list,
        {},
    )


def word_filter(word_list: list[str]) -> dict[str, int]:
    return {
        word: len(list(filter(lambda x: x == word, word_list)))
        for word in set(word_list)
    }


def word_counter(word_list: list[str]) -> dict[str, int]:
    return dict(Counter(word_list))


def print_examples(sentence: str) -> None:
    lst = clean_sentence(sentence)
    fn_list = [
        word_count(lst),
        word_reduce(lst),
        word_filter(lst),
        word_counter(lst),
    ]
    for fn in fn_list:
        print(fn)


if __name__ == '__main__':
    sentence: str = (
        'She went to the store to buy apples. She buys apples for apple tarts.'
    )
    print_examples(sentence)
