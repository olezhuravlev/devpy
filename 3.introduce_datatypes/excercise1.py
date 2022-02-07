#!/usr/bin/python3

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


def match():
    if (len(boys) != len(girls)):
        print("Cannot match!")
        return

    boys.sort()
    girls.sort()

    print("Ideal pairs:")
    for boy, girl in zip(boys, girls):
        print(boy + " and " + girl)


if __name__ == '__main__':
    match()
