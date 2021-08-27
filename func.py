"""Описание основных функций игры."""
import copy
import time
import random
from typing import Any

from classes_bridge import *
from totem_memento import *


class Game(Character):
    def __init__(self):
        self.hero = None
        self.caretaker = None
        self.enemy = None

    def choose_hero(self) -> None:
        """Выбор персонажа."""
        print("Добро пожаловать в игру!\n")
        while True:
            print("\t Выбери персонажа, в роли которого хочешь пройти эту игру: ")
            print("\t Введи [1] --> Paladin - класс воина, имеет преимущество при атаке в ближнем бою.")
            print("\t Введи [2] --> Ranger - класс лучника, имеет преимущество при атаке лучников.")
            print("\t Введи [3] --> Sorcerer - класс мага, имеет преимущество при магической атаке.")
            option = int(input('\t Выбранная опция: '))
            if option < 1 or option > 3:
                print('\n\t Выбери валидную опцию!')
                continue
            else:
                break
        if option == 1:
            hero = Warrior(10, 20)
        elif option == 2:
            hero = Archer(10, 15)
        elif option == 3:
            hero = Mage(10, 15)

        self.hero = hero

    def game_play(self) -> None:
        """с помощью этой функции происходит произвольный выбор следующего действия."""
        if self.hero.enemy_counter == 10:
            self.game_over(1)
        else:
            while True:
                print("\nЧтоб продолжить приключение - введи 1, отказаться - введи 2.")
                i = int(input())
                if i == 1:
                    break
                elif i == 2:
                    self.game_over(2)
                else:
                    print("\nНекорректное значение.")

        random_g = random.choices([1, 2, 3, 4, 5, 6, 7], weights=[1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3])[0]
        if random_g == 1:
            self.enemy_game()
        elif random_g == 2:
            self.sword_attr()
        elif random_g == 3:
            self.archer_attr()
        elif random_g == 4:
            self.arrow_attr()
        elif random_g == 5:
            self.mage_attr()
        elif random_g == 6:
            self.totem_attr()
        elif random_g == 7:
            self.apple_attr()

    def enemy_game(self) -> None:
        """функция описывает действие с монстром."""
        print("\nСтоило тебе сделать пару шагов – из-за угла появляется твой враг!")
        random_m = random.randint(1, 3)
        if random_m == 1:
            enemy_health = random.randint(1, 10)
            enemy_attack = random.randint(1, 10)
            Warrior.enemy(enemy_health, enemy_attack)
        elif random_m == 2:
            enemy_health = random.randint(1, 10)
            enemy_attack = random.randint(1, 10)
            Archer.enemy(enemy_health, enemy_attack)
        elif random_m == 3:
            enemy_health = random.randint(1, 10)
            enemy_attack = random.randint(1, 10)
            Mage.enemy(enemy_health, enemy_attack)

        while True:
            print("\nХочешь смело подраться с врагом ? – введи 1, хочешь шустро смыться - введи 2")
            i = int(input())
            if i == 1:
                while True:
                    print("\nВыбери оружие, которое хочешь использовать для текущей атаки:")
                    print("\t'1' - атака мечом, '2' - атака луком, '3' - магическая атака.")
                    i = int(input())
                    if i == 1:
                        hero_attack = self.hero.sword_attack
                        print("Сила твоей атаки в этом бою = ", hero_attack)
                    elif i == 2:
                        hero_attack = self.hero.bow_attack
                        print("Сила твоей атаки в этом бою = ", hero_attack)
                    elif i == 3:
                        hero_attack = self.hero.magic_attack
                        print("Сила твоей атаки в этом бою = ", hero_attack)
                    else:
                        print("Некорректное значение. Введи: '1' - атака мечом, "
                              "'2' - атака луком, '3' - магическая атака.")

                if ((Warrior.hero and Warrior.enemy) or (Archer.hero and Archer.enemy) or (Mage.hero and Mage)):
                    # Определение случайной защиты героя от атак своего класса
                    print("Давай посмотрим, насколько тебе сопутсвует удача в этом бою?..")
                    b = input(print("Нажми enter, чтобы бросить кости..."))
                    time.sleep(.5)
                    print('Кости брошены...')
                    defence = random.randint(3, 10)
                    print(f"Ты достаешь из-за спины свой щит, который защитит тебя от {defence} из 10 единиц урона.")

                print("Идет битва не на жизнь,а на смерть...")
                time.sleep(.5)
                if self.hero.health > enemy_attack:
                    self.hero.health = self.hero.health - enemy_attack
                    if hero_attack > enemy_health:
                        print("Ты безжалостно убиваешь своего врага!!!")
                        enemy_counter = enemy_counter + 1
                    else:
                        print("Твой враг оказался достаточно силён, после твоего удара ему удалось убежать.")
                        print("Ты остался жив, но монстр отнимает у тебя ", enemy_attack, " единиц здоровья", )
                else:
                    print("Сила атаки врага превосходит твое здоровье, он беспощадно тебя убивает...")
                    if totem == 1:
                        # поднять историю снимка из totem_memento
                        self.caretaker.show_history()
                        # восстановить снимок из totem_memento
                        self.caretaker.undo()
                    else:
                        self.game_over(3)
                break
            elif i == 2:
                print("\nТы успешно смылся от этого монстра! Можешь набраться сил и продолжить.")
                break
            else:
                print("Некорректное значение. Чтоб продолжить приключение - введи 1, отказаться - введи 2.")

    def sword_attr(self) -> None:
        """функция описывает действие с мечом."""
        print("\nНа миг в твоих глазах помутнело от блеска – перед тобой в воздухе парит новый МЕЧ.")
        if Warrior.hero:
            a = random.randint(5, 20)
            Hero.set_sword_attack(self.hero, a)
        else:
            a = random.randint(5, 12)
            Hero.set_sword_attack(self.hero, a)
        print("Сила атаки этого меча = ", a)
        print("Чтобы взять меч себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                print("С новым мечом сила твоей атаки в ближнем бою равна ", Hero.get_sword_attack)
                break
            elif i == 2:
                break
            else:
                print("Некорректное значение. Чтобы взять меч себе - введи 1, пройти мимо - введи 2.")
        self.game_play()

    def archer_attr(self) -> None:
        """функция описывает действие с луком."""
        print("\nНа твоем пути встречается новый ЛУК.")
        if Archer.hero:
            a = random.randint(5, 20)
            Hero.set_bow_attack(self.hero, a)
        else:
            a = random.randint(5, 12)
            Hero.set_bow_attack(self.hero, a)
        print("Сила атаки этого лука = ", a)
        print("Чтобы взять лук себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                print("С новым луком сила твоей атаки лучника равна ", Hero.get_bow_attack())
                break
            elif i == 2:
                break
            else:
                print("Некорректное значение. Чтобы взять лук себе - введи 1, пройти мимо - введи 2.")
        self.game_play()

    def arrow_attr(self) -> None:
        """функция описывает действие со стрелами для лука."""
        print("\nИдешь дальше... и спотыкаешься о колчан со стрелами.")
        arrow_count = random.randint(5, 12)
        print("В колчане ", arrow_count, " стрел для твоего лука")
        print("Чтобы взять колчан себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                Hero.set_arrow(self.hero, arrow_count)
                print("Теперь ты можешь использовать свой лук в бою.")
                break
            elif i == 2:
                break
            else:
                print("Некорректное значение. Чтобы взять колчан себе - введи 1, пройти мимо - введи 2.")
        self.game_play()

    def mage_attr(self) -> None:
        """функция описывает действие с книгой заклинаний."""
        print("\nУ тебя перед носом из пустоты возникает книга заклинаний.")
        if Mage.hero:
            a = random.randint(5, 20)
            Hero.set_magic_attack(self.hero, a)
        else:
            a = random.randint(5, 12)
            Hero.set_magic_attack(self.hero, a)
        print("Сила магической атаки этой волшебной книги заклинаний = ", a)
        print("Чтобы взять себе - введи 1, пройти мимо - введи 2")
        self.game_play()

        while True:
            i = int(input())
            if i == 1:
                print("С новой книгой заклинаний сила твоей магической атаки равна ", Hero.get_magic_attack)
                break
            elif i == 2:
                break
            else:
                print("Некорректное значение. Чтобы взять себе - введи 1, пройти мимо - введи 2.")

        self.game_play()

    def totem_attr(self) -> None:
        """функция описывает действие с тотемом."""
        print("\nНа своем пути ты видишь на полу сверкающий предмет... Да это же Тотем для сохранения игры!!!.")
        print("Чтобы взять себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                Hero.set_totem(self.hero, 1)
                print("Теперь у тебя есть ", Hero.get_totem(self.hero), " тотем - шанс, в случае гибели,"
                                                                        " вернуться снова к текущему моменту игры!")
                # создание снимка в totem_memento - текущие параметры героя
                hero_copy = copy.deepcopy(self.hero)
                originator = Originator(hero_copy)  # в скобки нужно вставить текущие параметры героя
                # сохранение состояния снимка в totem_memento
                self.caretaker = Caretaker(originator)
                # бэкап снимка в totem_memento
                self.caretaker.backup()
                break
            elif i == 2:
                break
            else:
                print("Некорректное значение. Чтобы взять себе - введи 1, пройти мимо - введи 2.")
            self.game_play()

    # self.game_play убрать и поменять местами 257 и 258
    def apple_attr(self) -> None:
        """функция описывает действие с яблоком."""
        print("\nПо пути ты видишь на полу сочное и спелое яблоко.")
        print("Бежишь к нему, спотыкаясь, чтоб скорее подкрепиться и добавить себе жизненной силы")
        apple = random.randint(3, 10)

        print("Ты стал мощнее! Сочное яблоко добавляет тебе ", apple, " единиц здоровья")
        Hero.set_health(self.hero, apple)
        self.game_play()

    def game_over(flag: int) -> int:
        """функция описывает завершение игры."""
        if flag == 1:
            print("Игра завершена. Ты побил всех монстров. ПОБЕДА!!!")
        elif flag == 2:
            print("Игра завершена!")
        elif flag == 3:
            print("Игра завершена. Ты потерпел ПОРАЖЕНИЕ:( ")
