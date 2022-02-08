#!/usr/bin/python3

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def get_visits(country):
    result = []
    for visit in geo_logs:
        for visit_name, visit_points in visit.items():
            if visit_points[1] == country:
                result.append({visit_name: visit_points})

    return result


if __name__ == '__main__':
    country_visits = get_visits("Россия")
    print(country_visits)
