#!/usr/bin/python3

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def get_unique():

    result = set()

    for user, geos in ids.items():
        result.update(geos)

    return result


if __name__ == '__main__':
    unique_geos = get_unique()
    print(unique_geos)
