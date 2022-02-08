#!/usr/bin/python3

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def get_max():
    max_name = ""
    max_value = 0
    for key, value in stats.items():
        if value > max_value:
            max_name = key
            max_value = value

    return max_name


if __name__ == '__main__':
    best_seller = get_max()
    print(best_seller)
