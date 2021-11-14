"""Описание основных функций игры."""
import copy
import time
import random
from typing import Any

from classes_bridge import *
from totem_memento import *


class Game(Specificity):
    def __init__(self):
        self.actor: Hero = None
        self.monster: Enemy = None
        self.caretaker = None
        self.actor_power = None

    def choose_hero(self) -> Any:
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
            actor = Hero(Warrior(), 15)
            actor.set_sword(14)
            actor.display_description()
            time.sleep(.5)
            self.actor = actor  # Warrior.class_type
            return self.actor
        elif option == 2:
            actor = Hero(Archer(), 15)
            actor.set_sword(10)
            actor.display_description()
            time.sleep(.5)
            self.actor = actor  # Archer.class_type
            return self.actor
        elif option == 3:
            actor = Hero(Mage(), 15)
            actor.set_sword(10)
            actor.display_description()
            time.sleep(.5)
            self.actor = actor  # Mage.class_type
            return self.actor

    def game_play(self) -> None:
        """с помощью этой функции происходит произвольный выбор следующего действия."""
        if self.actor.enemy_counter == 5:
            self.game_over(1)
        else:
            random_g = random.choices([1, 2, 3, 4, 5, 6, 7], weights=[1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3])[0]
            if random_g == 1:
                time.sleep(.5)
                self.enemy_game()
            elif random_g == 2:
                time.sleep(.5)
                self.sword_attr()
            elif random_g == 3:
                time.sleep(.5)
                self.archer_attr()
            elif random_g == 4:
                time.sleep(.5)
                self.arrow_attr()
            elif random_g == 5:
                time.sleep(.5)
                self.mage_attr()
            elif random_g == 6:
                time.sleep(.5)
                self.totem_attr()
            elif random_g == 7:
                time.sleep(.5)
                self.apple_attr()

    def select_weapon(self) -> Any:
        while True:
            print("\nВыбери оружие, которое хочешь использовать для текущей атаки:")
            print("\t'1' - атака мечом, '2' - атака луком, '3' - магическая атака.")
            i = int(input())
            if i == 1:
                if self.actor.get_sword() != 0:
                    self.actor_power = self.actor.get_sword()
                    print("Сила твоей атаки в этом бою = ", self.actor_power)
                    return self.actor_power
                else:
                    print("Невозможно воспользовать оружием, которого нет. Выбери что-то из твоего арсенала.")
                    continue
            elif i == 2:
                if self.actor.get_bow() and self.actor.get_arrow() != 0:
                    self.actor_power = self.actor.get_bow()
                    print("Сила твоей атаки в этом бою = ", self.actor_power)
                    return self.actor_power
                else:
                    print("Невозможно воспользовать оружием, которого нет. Выбери что-то из твоего арсенала.")
                    continue
            elif i == 3:
                if self.actor.get_magic() != 0:
                    self.actor_power = self.actor.get_magic()
                    print("Сила твоей атаки в этом бою = ", self.actor_power)
                    return self.actor_power
                else:
                    print("Невозможно воспользовать оружием, которого нет. Выбери что-то из твоего арсенала.")
                    continue
            else:
                print("Некорректное значение. Введи: '1' - атака мечом, "
                      "'2' - атака луком, '3' - магическая атака.")

    def set_defence(self) -> None:
        """Определение случайной защиты героя от атак своего класса."""
        if self.actor.get_class_type() == self.monster.get_class_type():
            print("Давай посмотрим, насколько тебе сопутсвует удача в этом бою?..")
            print("Нажми enter, чтобы бросить кости...")
            input()
            time.sleep(.5)
            print('Кости брошены...')
            defence = random.randint(3, 10)
            print(f"Ты достаешь из-за спины свой щит, который защитит тебя от {defence} из 10 единиц урона.")
            self.actor.set_defence(defence)
            aa = self.monster.get_power() - self.actor.get_defence()
            self.monster.set_power(aa)

    def enemy_game(self) -> Any:
        """функция описывает действие с монстром."""
        print("\nСтоило тебе сделать пару шагов – из-за угла появляется твой враг!")
        random_m = random.randint(1, 3)
        if random_m == 1:
            monster = Enemy(Warrior())
            monster.display_description()
            self.monster = monster  # Warrior.class_type
        elif random_m == 2:
            monster = Enemy(Archer())
            monster.display_description()
            self.monster = monster  # Archer.class_type
        elif random_m == 3:
            monster = Enemy(Mage())
            monster.display_description()
            self.monster = monster  # Mage.class_type

        while True:
            self.actor.display_description()
            print("\nХочешь смело подраться с врагом ? – введи 1, хочешь шустро смыться - введи 2")
            i = int(input())
            if i == 1:
                self.select_weapon()
                self.set_defence()
                print("Идет битва не на жизнь,а на смерть...")
                time.sleep(.5)
                if self.actor.get_health() > self.monster.get_power():
                    bb = self.actor.get_health() - self.monster.get_power()
                    self.actor.set_health(bb)
                    if self.actor_power > self.monster.get_health():
                        print("\nТы безжалостно убиваешь своего врага!!!")
                        self.actor.set_enemy_counter(1)
                        time.sleep(.5)
                    else:
                        print("\nТвой враг оказался достаточно силён, после твоего удара ему удалось убежать.")
                        print("Ты остался жив, но монстр отнимает у тебя ", self.monster.get_power(),
                              " единиц здоровья", )
                        time.sleep(.5)
                else:
                    print("\nСила атаки врага превосходит твое здоровье, он беспощадно тебя убивает...")
                    if self.actor.get_totem() == 1:
                        # поднять историю снимка из totem_memento
                        self.caretaker.show_history()
                        # восстановить снимок из totem_memento
                        self.caretaker.undo()
                        self.actor.set_totem(0)
                        time.sleep(.5)
                    else:
                        self.game_over(3)
                break
            elif i == 2:
                print("\nТы успешно смылся от этого монстра! Можешь набраться сил и продолжить.")
                break
            else:
                print("Некорректное значение. Чтоб продолжить приключение - введи 1, отказаться - введи 2.")
        self.game_play()

    def sword_attr(self) -> None:
        """функция описывает действие с мечом."""
        print("\nНа миг в твоих глазах помутнело от блеска – перед тобой в воздухе парит новый МЕЧ.")
        if self.actor.get_class_type() == "Warrior":
            power = random.randint(10, 18)
        else:
            power = random.randint(5, 12)

        print("Сила атаки этого меча = ", power)
        print("Чтобы взять меч себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                self.actor.set_sword(power)
                print("С новым мечом сила твоей атаки в ближнем бою равна ", self.actor.get_sword())
                break
            elif i == 2:
                break
            else:
                print("Некорректное значение. Чтобы взять меч себе - введи 1, пройти мимо - введи 2.")
        self.game_play()

    def archer_attr(self) -> None:
        """функция описывает действие с луком."""
        print("\nНа твоем пути встречается новый ЛУК.")
        if self.actor.get_class_type() == "Archer":
            power = random.randint(10, 18)
        else:
            power = random.randint(5, 12)
        print("Сила атаки этого лука = ", power)
        print("Чтобы взять лук себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                self.actor.set_bow(power)
                print("С новым луком сила твоей атаки лучника равна ", self.actor.get_bow())
                break
            elif i == 2:
                break
            else:
                print("Некорректное значение. Чтобы взять лук себе - введи 1, пройти мимо - введи 2.")
        self.game_play()

    def arrow_attr(self) -> None:
        """функция описывает действие со стрелами для лука."""
        print("\nИдешь дальше... и спотыкаешься о колчан со стрелами.")
        arrow_count = random.randint(3, 8)
        print("В колчане ", arrow_count, " стрел для твоего лука")
        print("Чтобы взять колчан себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                self.actor.set_arrow(arrow_count)
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
        if self.actor.get_class_type() == "Mage":
            power = random.randint(10, 18)
        else:
            power = random.randint(5, 12)
        print("Сила магической атаки этой волшебной книги заклинаний = ", power)
        print("Чтобы взять себе - введи 1, пройти мимо - введи 2")

        while True:
            i = int(input())
            if i == 1:
                self.actor.set_magic(power)
                print("С новой книгой заклинаний сила твоей магической атаки равна ", self.actor.get_magic())
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
                self.actor.set_totem(1)
                print("Теперь у тебя есть ", self.actor.get_totem(), " тотем - шанс, в случае гибели,"
                                                                     " вернуться снова к текущему моменту игры!")
                # создание снимка в totem_memento - текущие параметры героя
                aa = (self.actor.get_class_type, self.actor.get_health, self.actor.get_sword, self.actor.get_bow,
                      self.actor.get_magic, self.actor.get_arrow, self.actor.get_totem, self.actor.get_enemy_counter)
                hero_copy = copy.deepcopy(aa)
                originator = Originator(hero_copy)
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

    def apple_attr(self) -> None:
        """функция описывает действие с яблоком."""
        print("\nПо пути ты видишь на полу сочное и спелое яблоко.")
        print("Бежишь к нему, спотыкаясь, чтоб скорее подкрепиться и добавить себе жизненной силы")
        apple = random.randint(1, 7)

        print("Ты стал мощнее! Сочное яблоко добавляет тебе ", apple, " единиц здоровья")
        bb = self.actor.get_health() + apple
        self.actor.set_health(bb)
        print("Теперь твое здоровье = ", self.actor.get_health())
        self.game_play()

    def game_over(self, flag: int) -> None:
        """функция описывает завершение игры."""
        if flag == 1:
            print("Игра завершена. Ты побил всех монстров. ПОБЕДА!!!")
            exit()
        elif flag == 2:
            print("Игра завершена!")
            exit()
        elif flag == 3:
            print("Игра завершена. Ты потерпел ПОРАЖЕНИЕ:( ")
            exit()
