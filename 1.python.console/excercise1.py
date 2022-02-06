#!/usr/bin/python3

def hello_world():
    print("Hello, World!")


def arithmetic():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a + b)
    print(a - b)
    print(a * b)


if __name__ == '__main__':
    hello_world()
    arithmetic()
