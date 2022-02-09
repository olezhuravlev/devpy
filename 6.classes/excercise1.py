class Animal:

    def __init__(self, attribute, weight):
        self.attribute = attribute
        self.weight = weight

    def feed(self):
        print(self.__class__, self.attribute, "is fed!")

    def shout(self):
        pass


class Bird(Animal):
    def gatherErrs(self):
        print("Eggs of", self.__class__, self.attribute, "gathered!")

    def shout(self):
        print(self.__class__, self.attribute, "says: Tweet-tweet!")


class Goose(Bird):
    def shout(self):
        print(self.__class__, self.attribute, "says: Ga-ga-ga!")


class Hen(Bird):
    def shout(self):
        print(self.__class__, self.attribute, "says: Co-co-co!")


class Duck(Bird):
    def shout(self):
        print(self.__class__, self.attribute, "says: Crya-crya!")


class Cow(Animal):
    def milk(self):
        print("Milk of", self.__class__, self.attribute, "collected.")

    def shout(self):
        print(self.__class__, self.attribute, "says: Muuuuuuu!")


class Sheep(Animal):
    def cut(self):
        print("Wool of", self.__class__, self.attribute, "cut off.")

    def shout(self):
        print(self.__class__, self.attribute, "says: Meeeeee!")


class Goat(Animal):
    def shout(self):
        print(self.__class__, self.attribute, "says: Beeeeee!")


def test(animals_list):
    for animal in animals_list:
        animal.feed()
        animal.shout()
        if isinstance(animal, Bird):
            animal.gatherErrs()
        elif isinstance(animal, Cow):
            animal.milk()
        elif isinstance(animal, Sheep):
            animal.cut()


def count_weight(animals_list):
    return sum(anim.weight for anim in animals_list)


def find_haviest(animals_list):
    max = 0
    attribute = ""
    for animal in animals_list:
        if animal.weight > max:
            max = animal.weight
            attribute = animal.attribute

    return attribute


if __name__ == '__main__':
    animals = [Goose("Gray", 3), Goose("Gray", 3), Goose("White", 3.2), Cow("Manyka", 350), Sheep("Lamb", 45),
               Sheep("Curly", 43), Hen("Co-Co", 1.5), Hen("Cu-ca-re-cu", 1.3), Goat("Horns", 34), Goat("Hooves", 38),
               Duck("Cryakva", 2.4)]

    test(animals)

    print(count_weight(animals))
    print(find_haviest(animals))
