#!/usr/bin/python3
import Utils


def estimate(height, age, children, is_student):
    if (18 < age < 27 and not children and not is_student):
        if (height < 170):
            print("Tankman")
        elif (height < 180):
            print("Navy")
        elif (height < 200):
            print("Commando")
        else:
            print("Other military branch")
    else:
        print("Cannot be enlisted")


if __name__ == '__main__':
    age = Utils.get_parameter("Enter age: ")
    height = Utils.get_parameter("Enter height: ")
    children = Utils.get_parameter("Enter amount of children: ")
    is_student = Utils.get_parameter("Is a student?: ")
    estimate(height, age, children, is_student)
