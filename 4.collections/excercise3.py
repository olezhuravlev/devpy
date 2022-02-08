#!/usr/bin/python3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


def get_statistic(ndigits):
    result = dict()

    # Count occurrences.
    for query in queries:
        count = query.strip().count(" ") + 1
        already = result.get(count, 0)
        result[count] = already + 1

    # Count and format percents.
    total = sum(result.values())
    for key, value in result.items():
        share = value / total
        result[key] = str(round(share * 100, ndigits)) + "%";

    return result


if __name__ == '__main__':
    word_statistic = get_statistic(2)
    print(word_statistic)
