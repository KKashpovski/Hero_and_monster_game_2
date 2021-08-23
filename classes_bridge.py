"""Паттерн проектирования Мост(Bridge) для классификации героев и монстров."""


from __future__ import annotations
from abc import ABC, abstractmethod
import random


class Character:
    """
    Класс устанавливает интерфейс для «управляющей» части двух иерархий
    классов (героев и чудовищ). Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настоящую работу.
    """
    # Класс персонажа как героя, так и врага может быть: Воин/Warrior, Лучник/Archer, Маг/Mage

    def __init__(self, health, sword_attack, bow_attack, magic_attack):
        """Характеристики персонажа."""
        # здоровье
        self.health = health
        # сила атаки ближнего боя (меч)
        self.sword = sword_attack
        # сила атаки лучника (лук)
        self.bow = bow_attack
        # сила магической атаки (заклинания)
        self.magic = magic_attack

    def sethealth(self, health):
        """Здоровье."""
        self.health = health

    def setsword(self, sword_attack):
        """Меч."""
        self.sword = sword_attack

    def setbow(self, bow_attack):
        """Лук."""
        self.bow = bow_attack

    def setmagic(self, magic_attack):
        """Книга заклинаний."""
        self.magic = magic_attack

    def gethealth(self):
        """Здоровье."""
        return self.health

    def getsword(self):
        """Меч."""
        return self.sword

    def getbow(self):
        """Лук."""
        return self.bow

    def getmagic(self):
        """Книга заклинаний."""
        return self.magic


class ExtendedCharacter(Character):
    """
    Можно расширить Абстракцию без изменения классов Реализации.
    """
    def __init__(self, health, sword_attack, bow_attack, magic_attack):
        """Характеристики персонажа."""
        super().__init__(health, sword_attack, bow_attack, magic_attack)
        # колическтво стрел для лука
        self.arrow = 0
        # случайная защита шероя от атак своего класса
        self.defence = 0
        # тотем/сохранение игры
        self.totem = 0
        # количество поверженных монстров
        self.monster_counter = 0

    def setarrow(self, arrow):
        self.arrow = arrow

    def setdefence(self, defence):
        self.arrow = defence

    def settotem(self, totem):
        self.arrow = totem

    def setmonster_counter(self, monster_counter):
        self.arrow = monster_counter

    def getarrow(self, arrow):
        self.arrow = arrow

    def getdefence(self, defence):
        self.arrow = defence

    def gettotem(self, totem):
        self.arrow = totem

    def getmonster_counter(self, monster_counter):
        self.arrow = monster_counter


class Hero(Character):
    """Характеристики героя."""
    def paladin(self, health, sword_attack, bow_attack, magic_attack, arrow, defence, totem, monster_counter):
        setattr(Hero, health, random.randint(8, 20))
        setattr(Hero, sword_attack, random.randint(5, 20))
        setattr(Hero, bow_attack, 0)
        setattr(Hero, magic_attack, 0)
        setattr(Hero, arrow, 0)
        setattr(Hero, defence, 0)
        setattr(Hero, totem, 0)
        setattr(Hero, monster_counter, 0)

    def ranger(self, health, sword_attack, bow_attack, magic_attack, arrow, defence, totem, monster_counter):
        setattr(Hero, health, random.randint(8, 20))
        setattr(Hero, sword_attack, random.randint(5, 12))
        setattr(Hero, bow_attack, 0)
        setattr(Hero, magic_attack, 0)
        setattr(Hero, arrow, 0)
        setattr(Hero, defence, 0)
        setattr(Hero, totem, 0)
        setattr(Hero, monster_counter, 0)

    def sorcerer(self, health, sword_attack, bow_attack, magic_attack, arrow, defence, totem, monster_counter):
        setattr(Hero, health, random.randint(8, 20))
        setattr(Hero, sword_attack, random.randint(5, 12))
        setattr(Hero, bow_attack, 0)
        setattr(Hero, magic_attack, 0)
        setattr(Hero, arrow, 0)
        setattr(Hero, defence, 0)
        setattr(Hero, totem, 0)
        setattr(Hero, monster_counter, 0)


class Enemy(Character):
    """Характеристики врага."""
    def goblin(self, health, sword_attack, bow_attack, magic_attack):
        setattr(Enemy, health, random.randint(8, 20))
        setattr(Enemy, sword_attack, random.randint(5, 12))
        setattr(Enemy, bow_attack, random.randint(5, 12))
        setattr(Enemy, magic_attack, random.randint(5, 12))

    def dark_elf(self, health, sword_attack, bow_attack, magic_attack):
        setattr(Enemy, health, random.randint(8, 20))
        setattr(Enemy, sword_attack, random.randint(5, 12))
        setattr(Enemy, bow_attack, random.randint(5, 12))
        setattr(Enemy, magic_attack, random.randint(5, 12))

    def necromancer(self, health, sword_attack, bow_attack, magic_attack):
        setattr(Enemy, health, random.randint(8, 20))
        setattr(Enemy, sword_attack, random.randint(5, 12))
        setattr(Enemy, bow_attack, random.randint(5, 12))
        setattr(Enemy, magic_attack, random.randint(5, 12))


class Attack(ABC):
    """
    Реализация устанавливает интерфейс для всех классов реализации. Он не должен
    соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
    совершенно разными. Как правило, интерфейс Реализации предоставляет только
    примитивные операции, в то время как Абстракция определяет операции более
    высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def warrior_attack(self):
        pass

    def archer_attack(self):
        pass

    def mage_attack(self):
        pass


class WarriorAttack(Attack):
    """Атака ближнего боя для каждого класса персонажей."""
    def warrior_attack(self):
        pass

    def archer_attack(self):
        pass

    def mage_attack(self):
        pass


class ArcherAttack(Attack):
    """Атака луком для каждого класса персонажей."""
    def warrior_attack(self):
        pass

    def archer_attack(self):
        pass

    def mage_attack(self):
        pass


class MageAttack(Attack):
    """Магическая атака боя для каждого класса персонажей."""
    def warrior_attack(self):
        pass

    def archer_attack(self):
        pass

    def mage_attack(self):
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
