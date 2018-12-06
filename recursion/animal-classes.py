from random import randint


# Base Class
class Animal:
    # All of the classes take these values as part of their constructors and pass them up the chain to here
    # any arguments with an equals are default ones, if we don't need to change any we can miss them out
    def __init__(self, latin_name, common_name, weight, house_pet=False):
        self.latin_name = latin_name
        self.common_name = common_name
        self.weight = weight
        self.house_pet = house_pet

    def get_latin_name(self):
        return self.latin_name

    def get_common_name(self):
        return self.common_name

    def get_weight(self):
        return self.weight

    def is_house_pet(self):
        return self.house_pet


# Mammal inherits from Animal
class Mammal(Animal):
    def __init__(self, latin_name, common_name, weight, house_pet=False,
                 carnivore=False, herbivore=False, omnivore=False):
        # Notice the call to the parent constructor passing in the values (but not self)
        super().__init__(latin_name, common_name, weight, house_pet)
        self.carnivore = carnivore
        self.herbivore = herbivore
        self.omnivore = omnivore

    def is_carnivore(self):
        return self.carnivore

    def is_herbivore(self):
        return self.herbivore

    def is_omnivore(self):
        return self.omnivore


# Tiger inherits from Mammal (and ultimately from Animal)
class Tiger(Mammal):
    # I need to double check whether tiger_type would normally sit at the start of the parameter list or the end
    # as to me I would normally add the extra parameters to the end, but can't because we have default values.
    def __init__(self, tiger_type, latin_name, common_name, weight,
                 house_pet=False, carnivore=False, herbivore=False, omnivore=False):
        # Call the constructor for the Mammal class which will in turn call the Animal constructor
        super().__init__(latin_name, common_name, weight, house_pet, carnivore, herbivore, omnivore)
        self.type_of_tiger = tiger_type

    def get_type(self):
        return self.type_of_tiger


# Raccoon inherits from Mammal (and ultimately from Animal)
class Raccoon(Mammal):
    def __init__(self, latin_name, common_name, weight, house_pet=False,
                 carnivore=False, herbivore=False, omnivore=False):
        super().__init__(latin_name, common_name, weight, house_pet, carnivore, herbivore, omnivore)


# A bird is a type of Animal
class Bird(Animal):
    def __init__(self, latin_name, common_name, weight, house_pet=False, fly=False):
        super().__init__(latin_name, common_name, weight, house_pet)
        self.fly = fly

    def can_fly(self):
        return self.fly


# A crow inherits from Bird
class Crow(Bird):
    def __init__(self, latin_name, common_name, weight, house_pet=False, fly=True):
        super().__init__(latin_name, common_name, weight, house_pet, fly)


# A Penguin inherits from Bird
class Penguin(Bird):
    def __init__(self, latin_name, common_name, weight, house_pet=False, fly=False):
        super().__init__(latin_name, common_name, weight, house_pet, fly)


# Fish is a subclass of Animal
class Fish(Animal):
    def __init__(self, latin_name, common_name, weight, house_pet=False):
        super().__init__(latin_name, common_name, weight, house_pet)


# WhiteCatFish is a subclass of Fish
class WhiteCatFish(Fish):
    def __init__(self, latin_name, common_name, weight, house_pet=False, a_cat=False, a_fish=True):
        super().__init__(latin_name, common_name, weight, house_pet)
        self.a_cat = a_cat
        self.a_fish = a_fish

    def is_cat(self):
        return self.a_cat

    def is_fish(self):
        return self.a_fish


# Shark is a specialisation of Fish (or an extension)
class Shark(Fish):
    def __init__(self, latin_name, common_name, weight, house_pet=False, dangerous=True):
        super().__init__(latin_name, common_name, weight, house_pet)
        self.dangerous = dangerous

    def is_dangerous(self):
        return self.dangerous


class Menagerie:
    def __init__(self, animals):
        self.cages = list(animals)

some_animals = []
for x in range(100):
    beast = ""
    coin_toss = randint(1, 6)
    if coin_toss == 1:
        beast = Tiger("Stuffed", "Stufficus Tiggerus", "Stuffed Tigger", 1, True)
    elif coin_toss == 2:
        beast = Raccoon("Raccoonicus somethingus", "Rocket Raccoon", 3)
    elif coin_toss == 3:
        beast = Crow("Corvinus corvidii", "Storm Crow", 1)
    elif coin_toss == 4:
        beast = Penguin("Chocolatus Baricus", "Pingu", 2)
    elif coin_toss == 5:
        beast = WhiteCatFish("Albinus Felinicus Fishicus", "WCF", 4)
    elif coin_toss == 6:
        beast = Shark("Sharkus biggus toothicus", "Jaws", 60)
    some_animals.append(beast)

zoo = Menagerie(some_animals)

for exhibit in zoo.cages:
    print(exhibit.get_common_name())
