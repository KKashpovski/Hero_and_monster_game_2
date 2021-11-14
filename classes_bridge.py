import random
from abc import ABC, abstractmethod


class Specificity:
    class_type = None

    def hero(self, health, sword, bow, magic, arrow, totem, enemy_counter):
        pass

    def enemy(self, health, power):
        pass


class Warrior(Specificity):
    class_type = "Warrior"

    def hero(self, health, sword, bow, magic, arrow, totem, enemy_counter):
        print("\nТы относишься к классу", self.class_type, "и обладаешь следующими характеристиками, Paladin:")
        print("\n\tЗдоровье героя = ", health,
              "\n\tСила атаки меча в ближнем бою = ", sword,
              "\n\tСила атаки лука = ", bow,
              "\n\tСила магической атаки = ", magic,
              "\n\tКоличество стрел = ", arrow,
              "\n\tНаличие тотема = ", totem,
              "\n\tКоличество поверженных монстров = ", enemy_counter)

    def enemy(self, health, power):
        print("\nТвой враг Goblin, относится к классу", self.class_type, "и обладает следующими характеристиками:")
        print("\n\tЗдоровье врага = ", health, "\n\tСила атаки меча в ближнем бою = ", power)


class Archer(Specificity):
    class_type = "Archer"

    def hero(self, health, sword, bow, magic, arrow, totem, enemy_counter):
        print("\nТы относишься к классу", self.class_type, "и обладаешь следующими характеристиками, Ranger:")
        print("\n\tЗдоровье героя = ", health,
              "\n\tСила атаки меча в ближнем бою = ", sword,
              "\n\tСила атаки лука = ", bow,
              "\n\tСила магической атаки = ", magic,
              "\n\tКоличество стрел = ", arrow,
              "\n\tНаличие тотема = ", totem,
              "\n\tКоличество поверженных монстров = ", enemy_counter)

    def enemy(self, health, power):
        print("\nТвой враг DarkElf, относится к классу", self.class_type, "и обладает следующими характеристиками:")
        print("\n\tЗдоровье врага = ", health, "\n\tСила атаки лука = ", power)


class Mage(Specificity):
    class_type = "Mage"

    def hero(self, health, sword, bow, magic, arrow, totem, enemy_counter):
        print("\nТы относишься к классу", self.class_type, "и обладаешь следующими характеристиками, Sorcerer:")
        print("\n\tЗдоровье героя = ", health,
              "\n\tСила атаки меча в ближнем бою = ", sword,
              "\n\tСила атаки лука = ", bow,
              "\n\tСила магической атаки = ", magic,
              "\n\tКоличество стрел = ", arrow,
              "\n\tНаличие тотема = ", totem,
              "\n\tКоличество поверженных монстров = ", enemy_counter)

    def enemy(self, health, power):
        print("\nТвой враг Necromancer, относится к классу", self.class_type, "и обладает следующими характеристиками:")
        print("\n\tЗдоровье врага = ", health, "\n\tСила магической атаки = ", power)


class Character(ABC):
    def __init__(self, Specificity):
        self.specificity = Specificity

    @abstractmethod
    def get_class_type(self):
        pass

    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def get_health(self):
        pass
    #
    # @abstractmethod
    # def set_health(self, new_health):
    #     pass
    #
    # @abstractmethod
    # def get_sword(self):
    #     pass
    #
    # @abstractmethod
    # def set_sword(self, new_health):
    #     pass
    #
    # @abstractmethod
    # def get_bow(self):
    #     pass
    #
    # @abstractmethod
    # def set_bow(self, new_health):
    #     pass
    #
    # @abstractmethod
    # def get_magic(self):
    #     pass
    #
    # @abstractmethod
    # def set_magic(self, new_health):
    #     pass
    #
    # @abstractmethod
    # def get_arrow(self):
    #     pass
    #
    # @abstractmethod
    # def set_arrow(self, new_health):
    #     pass
    #
    # @abstractmethod
    # def get_totem(self):
    #     pass
    #
    # @abstractmethod
    # def set_totem(self, new_health):
    #     pass
    #
    # @abstractmethod
    # def get_enemy_counter(self):
    #     pass
    #
    # @abstractmethod
    # def set_enemy_counter(self, new_health):
    #     pass
    #
    # @abstractmethod
    # def get_power(self):
    #     pass


class Hero(Character):
    def __init__(self, Specificity, health):
        super().__init__(Specificity)
        self.health = health
        self.sword = 0
        self.bow = 0
        self.magic = 0
        self.arrow = 0
        self.totem = 0
        self.enemy_counter = 0
        self.defence = 0

    def get_class_type(self):
        return self.specificity.class_type

    def display_description(self):
        self.specificity.hero(self.health, self.sword, self.bow, self.magic, self.arrow, self.totem, self.enemy_counter)

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    def get_defence(self):
        return self.defence

    def set_defence(self, new_defence):
        self.defence = new_defence

    def get_sword(self):
        return self.sword

    def set_sword(self, new_sword):
        self.sword = new_sword

    def get_bow(self):
        return self.bow

    def set_bow(self, new_bow):
        self.bow = new_bow

    def get_magic(self):
        return self.magic

    def set_magic(self, new_magic):
        self.magic = new_magic

    def get_arrow(self):
        return self.arrow

    def set_arrow(self, new_arrow):
        self.arrow = new_arrow

    def get_totem(self):
        return self.totem

    def set_totem(self, new_totem):
        self.totem = new_totem

    def get_enemy_counter(self):
        return self.enemy_counter

    def set_enemy_counter(self, new_enemy_counter):
        self.enemy_counter += new_enemy_counter


class Enemy(Character):
    def __init__(self, Specificity):
        super().__init__(Specificity)
        self.health = random.randint(3, 15)
        self.power = random.randint(3, 15)

    def get_class_type(self):
        return self.specificity.class_type

    def display_description(self):
        self.specificity.enemy(self.health, self.power)

    def get_health(self):
        return self.health

    def get_power(self):
        return self.power

    def set_power(self, new_power):
        self.power = new_power


if __name__ == "__main__":
    # client_code
    #
    a = Hero(Warrior(), 15)
    power = random.randint(5, 12)
    a.set_sword(power)
    a.display_description()
    a.get_sword()
    # #
    # b = Hero(Archer(), 15)
    # b.display_description()
    # #
    # c = Hero(Mage(), 15)
    # c.display_description()
    # #
    # d = Enemy(Warrior())
    # d.display_description()
    # #
    # e = Enemy(Archer())
    # e.display_description()
    #
    f = Enemy(Mage())
    f.display_description()
