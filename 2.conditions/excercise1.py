#!/usr/bin/python3

def estimate(val):
    if (val % 2 > 0):
        print("Weird")
    else:
        if (2 <= val <= 5):
            print("Not Weird")
        elif (6 <= val <= 20):
            print("Weird")
        elif (20 < val):
            print("Not Weird")


if __name__ == '__main__':
    n = int(input("Enter a value: ").strip())
    estimate(n)
