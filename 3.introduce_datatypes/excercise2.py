#!/usr/bin/python3

import Utils

person = 5

cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]


def show_purchase_list(person):
    print("To buy for", str(person), "person:")
    for dish in cook_book:
        print(dish[0] + ":")
        for ingridient in dish[1]:
            print("\t", ingridient[0], ", ", ingridient[1] * person, "gr.", sep="")


if __name__ == '__main__':
    amount = Utils.get_parameter("Enter number of person: ", result_type=int, default=person)
    show_purchase_list(amount)
