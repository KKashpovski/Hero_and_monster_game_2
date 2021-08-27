"""Паттерн проектирования Мост(Bridge) для классификации героев и монстров."""

from __future__ import annotations
from abc import ABC, abstractmethod


class Character:
    """Характеристики персонажа. Применительны как к герою,так и к врагу."""
    def __init__(self, health, sword_attack):
        self.health = health
        self.sword_attack = sword_attack
        self.bow_attack = 0
        self.magic_attack = 0

    def get_health(self) -> int:
        """Здоровье."""
        return self.health

    def get_sword_attack(self) -> int:
         """Меч."""
         return self.sword_attack

    def get_bow_attack(self) -> int:
         """Лук."""
         return self.bow_attack
    #
    def get_magic_attack(self) -> int:
         """Магия."""
         return self.magic_attack
    #
    def set_health(self, new_health):
         """Здоровье."""
         self.health = new_health
    #
    def set_sword_attack(self, new_sword_attack):
         """Меч."""
         self.sword = new_sword_attack
    #
    def set_bow_attack(self, new_bow_attack):
         """Лук."""
         self.bow = new_bow_attack
    #
    def set_magic_attack(self, new_magic_attack):
         """Книга заклинаний."""
         self.magic = new_magic_attack


class ExtendedCharacter(Character):
    """Расширенные параметры. Применительны к герою."""

    def __init__(self, health, sword_attack):
        """Характеристики персонажа."""
        super().__init__(health, sword_attack)
        self.arrow = 0
        self.totem = 0
        self.enemy_counter = 0

    def get_arrow(self):
    #     """Стрелы."""
         return self.arrow

    def get_totem(self):
    #     """Тотем."""
         return self.totem
    #
    def get_enemy_counter(self):
    #     """Количество убитых монстров."""
         return self.enemy_counter
    #
    def set_arrow(self, new_arrow):
    #     """Стрелы."""
         self.arrow = new_arrow
    #
    def set_totem(self, new_totem):
    #     """Тотем."""
         self.totem = new_totem
    #
    def set_enemy_counter(self, new_enemy_counter):
    #     """Количество убитых монстров."""
         self.enemy_counter = new_enemy_counter


class Hero(ExtendedCharacter):
    """Характеристики героя."""

    def data_hero(self):
        print("\n\tЗдоровье героя = ", self.health,
              "\n\tСила атаки меча = ", self.sword_attack,
              "\n\tСила атаки лука = ", self.bow_attack,
              "\n\tСила магической атаки = ", self.magic_attack,
              "\n\tКоличество стрел = ", self.arrow,
              "\n\tНаличие тотема героя = ", self.totem,
              "\n\tКоличество поверженных монстров = ", self.enemy_counter)


class Enemy(Character):
    """Характеристики врага."""

    def data_enemy(self):
        print("\n\tЗдоровье врага = ", self.health,
              "\n\tСила атаки меча = ", self.sword_attack,
              "\n\tСила атаки лука = ", self.bow_attack,
              "\n\tСила магической атаки = ", self.magic_attack)


class Attack(ABC):
    """Интерфейс реализации ататки персонажей соответствующего класса."""

    def __init__(self, Character):
        self.character = Character

    @abstractmethod
    def hero(self):
        pass

    def enemy(self):
        pass


class Warrior(Hero):
    """Атака ближнего боя для каждого класса персонажей."""

    def __init__(self, health, sword_attack):
        super().__init__(health, sword_attack)

    def hero(self):
        print("\n Ты относишься к классу Warrior и обладаешь следующими характеристиками, Paladin: \n")
        print(self.health, self.sword_attack, self.bow_attack, self.magic_attack,
              self.arrow, self.totem, self.enemy_counter)

    def enemy(self):
        print("\n вой враг Goblin, он относится к классу Warrior и обладает следующими характеристиками: \n")
        print(self.health, self.sword_attack, self.bow_attack, self.magic_attack)


class Archer(Hero):
    """Атака луком для каждого класса персонажей."""

    def __init__(self, health, sword_attack):
        super().__init__(health, sword_attack)

    def hero(self):
        print("\n Ты относишься к классу Archer и обладаешь следующими характеристиками, Ranger: \n")
        print(self.health, self.sword_attack, self.bow_attack, self.magic_attack,
              self.arrow, self.totem, self.enemy_counter)

    def enemy(self):
        print("\n вой враг Dark_Elf, он относится к классу Archer и обладает следующими характеристиками: \n")
        print(self.health, self.sword_attack, self.bow_attack, self.magic_attack)


class Mage(Hero):
    """Магическая атака боя для каждого класса персонажей."""

    def __init__(self, health, sword_attack):
        super().__init__(health, sword_attack)

    def hero(self):
        print("\n Ты относишься к классу Mage и обладаешь следующими характеристиками, Sorcerer: \n")
        print(self.health, self.sword_attack, self.bow_attack, self.magic_attack,
              self.arrow, self.totem, self.enemy_counter)

    def enemy(self):
        print("\n Твой враг Necromancer, он относится к классу Mage и обладает следующими характеристиками: \n")
        print(self.health, self.sword_attack, self.bow_attack, self.magic_attack)


def client_code(abstraction: Abstraction) -> None:
#     """
#     За исключением этапа инициализации, когда объект Абстракции связывается с
#     определённым объектом Реализации, клиентский код должен зависеть только от
#     класса Абстракции. Таким образом, клиентский код может поддерживать любую
#     комбинацию абстракции и реализации.
#     """
#
#     # ...
#
#     print(abstraction.operation(), end="")
#
#     # ...
#
#
    if __name__ == "__main__":
#     """
#     Клиентский код должен работать с любой предварительно сконфигурированной
#     комбинацией абстракции и реализации.
#     """
#
        implementation = ConcreteImplementationA()
        abstraction = Abstraction(implementation)
        client_code(abstraction)
#     #
#     # print("\n")
#     #
        implementation = ConcreteImplementationB()
        abstraction = ExtendedAbstraction(implementation)
        client_code(abstraction)
