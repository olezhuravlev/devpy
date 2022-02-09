class SumList(list):
    def append(self, value):
        for item in self:
            if item["ingredient_name"] == value["ingredient_name"]:
                item["quantity"] = int(item["quantity"]) + int(value["quantity"])
                return

        # super().append(value)
        # list.append(self, value)
        super(SumList, self).append(value)


class Cookbook:
    def __init__(self, filename):
        self.cook_book = self.read_file(filename)

    def parse_row(self, row):
        words = row.split("|")
        if len(words) == 3:
            return {
                "ingredient_name": words[0].strip(),
                "quantity": words[1].strip(),
                "measure": words[2].strip()
            }
        elif len(words) == 1:
            return words[0].strip()
        else:
            return ""

    def read_file(self, filename):
        result = dict()

        with open(filename, encoding="UTF-8") as f:

            dish_title_row = True
            ingredients_count_row = True

            dish_title = ""
            ingredients = list()

            for row in f:
                if row.strip():
                    if dish_title_row:
                        dish_title = row.strip()
                        dish_title_row = False
                        ingredients_count_row = True
                    elif ingredients_count_row:
                        ingredients_count_row = False
                    else:
                        data = self.parse_row(row)
                        ingredients.append(data)
                else:
                    result[dish_title] = ingredients

                    dish_title_row = True
                    # ingredients_count_row = False
                    dish_title = ""
                    ingredients = list()

            result[dish_title] = ingredients

        return result

    def get_shop_list_by_dishes(self, dishes, persons=1):

        result = SumList()

        for dish in dishes:
            if dish in self.cook_book:
                for ingredient in self.cook_book[dish]:
                    result.append(ingredient)

        if persons == 1:
            return result

        for ingredient in result:
            ingredient["quantity"] = int(ingredient["quantity"]) * persons

        return result


if __name__ == '__main__':
    cook_book = Cookbook("recipes.txt")
    shop_list = cook_book.get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2);
    print(shop_list)
