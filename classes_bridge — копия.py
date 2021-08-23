"""Паттерн проектирования Мост(Bridge) для классификации героев и монстров."""


from __future__ import annotations
from abc import ABC, abstractmethod
import random


class Character:
    """Характеристики персонажа. Применительны как к герою,так и к врагу."""
    health = 0
    sword_attack = 0
    bow_attack = 0
    magic_attack = 0


class ExtendedCharacter(Character):
    """Расширенные параметры. Применительны к герою."""
    health = 0
    sword_attack = 0
    bow_attack = 0
    magic_attack = 0
    arrow = 0
    defence = 0
    totem = 0
    monster_counter = 0


class Hero(Character):
    """Характеристики героя."""
    @staticmethod
    def data_hero(health, sword_attack, bow_attack, magic_attack, arrow, defence, totem, monster_counter):
        print("\n\tЗдоровье героя = ", health,
              "\n\tСила атаки меча = ", sword_attack,
              "\n\tСила атаки лука = ", bow_attack,
              "\n\tСила магической атаки = ", magic_attack,
              "\n\tКоличество стрел = ", arrow,
              "\n\tУдача героя в бою своего класса = ", defence,
              "\n\tНаличие тотема героя = ", totem,
              "\n\tКоличество поверженных монстров = ", monster_counter)


class Enemy(Character):
    """Характеристики врага."""
    @staticmethod
    def data_enemy(health, sword_attack, bow_attack, magic_attack):
        print("\n\tЗдоровье врага = ", health,
              "\n\tСила атаки меча = ", sword_attack,
              "\n\tСила атаки лука = ", bow_attack,
              "\n\tСила магической атаки = ", magic_attack)


class Attack(ABC):
    """Интерфейс реализации ататки персонажей соответствующего класса."""
    def __init__(self, Character):
        self.character = Character

    @abstractmethod
    def attack_hero(self):
        pass

    def attack_enemy(self):
        pass


class Warrior(Attack):
    """Атака ближнего боя для каждого класса персонажей."""
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects
    def attack_hero(self):
        pass

    def attack_enemy(self):
        pass


class Archer(Attack):
    """Атака луком для каждого класса персонажей."""
    def attack_hero(self):
        pass

    def attack_enemy(self):
        pass


class Mage(Attack):
    """Магическая атака боя для каждого класса персонажей."""
    def attack_hero(self):
        pass

    def attack_enemy(self):
        pass


def client_code(abstraction: Abstraction) -> None:
    """
    За исключением этапа инициализации, когда объект Абстракции связывается с
    определённым объектом Реализации, клиентский код должен зависеть только от
    класса Абстракции. Таким образом, клиентский код может поддерживать любую
    комбинацию абстракции и реализации.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    Клиентский код должен работать с любой предварительно сконфигурированной
    комбинацией абстракции и реализации.
    """

    # implementation = ConcreteImplementationA()
    # abstraction = Abstraction(implementation)
    # client_code(abstraction)
    #
    # print("\n")
    #
    # implementation = ConcreteImplementationB()
    # abstraction = ExtendedAbstraction(implementation)
    # client_code(abstraction)
