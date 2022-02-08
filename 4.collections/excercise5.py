#!/usr/bin/python3


def convert_to_dict(source_list):
    result = dict()

    for idx in range(0, len(source_list), 4):
        result[source_list[idx]] = {source_list[idx + 1]: {source_list[idx + 2]: source_list[idx + 3]}}

    return result


if __name__ == '__main__':
    # my_list = ['2018-01-01', 'yandex', 'cpc', 100]
    # my_list2 = ['2018-01-01', 'yandex', 'cpc', 100, '2019-02-02', 'google', 'gl', 200]
    my_list3 = ['2018-01-01', 'yandex', 'cpc', 100, '2019-02-02', 'google', 'gl', 200, '2020-03-03', 'amazon', 'amz',
                300]
    dictionary = convert_to_dict(my_list3)
    print(dictionary)
