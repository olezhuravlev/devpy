#!/usr/bin/python3

import Utils


def main():
    salary = Utils.get_parameter("Enter month salary: ")

    while True:
        mortgage_share = Utils.get_parameter("Enter percent of salary spent for mortgage: ")
        spendings_share = Utils.get_parameter("Enter percent of salary spent to live on: ")
        if (mortgage_share + spendings_share > 100):
            print("Sum of the shares cannot exceed 100%!")
        else:
            break

    annual_salary = salary * 12
    annual_mortgage = annual_salary * mortgage_share / 100
    annual_spending = annual_salary * spendings_share / 100

    print("Your annual spending on mortgage: ", annual_mortgage)
    print("You will accumulate after a year: ", annual_salary - annual_mortgage - annual_spending)


if __name__ == '__main__':
    main()
