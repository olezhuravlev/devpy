#!/usr/bin/python3

import Utils

def main():
    square__length = Utils.get_parameter("Enter square side lenght: ")
    print("Perimeter:", square__length * 4)
    print("Square", square__length ** 2)

    rec_length = Utils.get_parameter("Enter square side lenght: ")
    rec_width = Utils.get_parameter("Enter square side width: ")
    print("Perimeter:", rec_length * 2 + rec_width * 2)
    print("Square", rec_length * rec_width)


if __name__ == '__main__':
    main()
