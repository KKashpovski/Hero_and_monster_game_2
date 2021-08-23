"""Описание основных функций игры."""


import random
from classes_bridge import *
from totem_memento import *
from typing import Any


def choose_hero() -> str:
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
        hero_name = "Paladin"
        return hero_name
    elif option == 2:
        hero_name = "Ranger"
        return hero_name
    elif option == 3:
        hero_name = "Sorcerer"
        return hero_name


def create_character(hero_name):
    if hero_name == "Paladin":
        print("\n Ты вступаешь в игру с мечом [сила атаки: 15 | защита: 10")
    elif hero_name == "Ranger":
        print("\n Ты вступаешь в игру с мечом [сила атаки: 11")
    elif hero_name == "Sorcerer":
        print("\n Ты вступаешь в игру с мечом [сила атаки: 8")
    print('\n\t Персонаж теперь обладает определенными навыками!')
    print('\n\t --- ПОСМОТРЕТЬ СТАТУС ---')



def random_ch() -> None:
    """с помощью этой функции происходит произвольный выбор следующего действия."""
    print("\nТвоя сила атаки = ", attack)
    print("Твое здоровье = ", hp)
    print("Количество поверженных героем монстров = ", monster_counter)
    if monster_counter == 10:
        game_over(1)
    else:
        while True:
            print("\nЧтоб продолжить приключение - введи 1, отказаться - введи 2.")
            i = int(input())
            if i == 1:
                break
            elif i == 2:
                game_over(2)
            else:
                print("\nНекорректное значение.")

    random_g = random.choices([1, 2, 3], weights=[0.6, 0.2, 0.4])[0]
    if random_g == 1:
        monster_game()
    elif random_g == 2:
        sword_game()
    elif random_g == 3:
        apple_game()


def monster_game() -> None:
    """функция описывает действие с монстром."""
    global monster_counter
    global hp
    monster_hp = random.randint(1, 12)
    monster_attack = random.randint(1, 12)
    print("\nСтоило тебе сделать пару шагов – из-за угла появляется коварный монстр")
    print(
        "Впереди тебя ждет серьезный БОЙ! Монстр имеет ",
        monster_hp,
        "жизней и сила его атаки ",
        monster_attack,
    )

    while True:
        print(
            "\nХочешь смело подраться с ним ? – введи 1, хочешь шустро смыться от монстра - введи 2"
        )
        i = int(input())
        if i == 1:
            print("Идет битва не на жизнь,а на смерть...")
            break
        elif i == 2:
            print(
                "\nТы успешно смылся от этого монстра! Можешь набраться сил и продолжить."
            )
            random_ch()
        else:
            print(
                "Некорректное значение. Чтоб продолжить приключение - введи 1, отказаться - введи 2."
            )

    if hp > monster_attack:
        hp = hp - monster_attack
        if attack > monster_hp:
            print("Ты безжалостно взмахиваешь мечом и убиваешь монстра!!!")
            monster_counter = monster_counter + 1
        else:
            print(
                "Монстр оказался достаточно крепким, после твоего удара ему удалось убежать неповерженным."
            )
            print(
                "Ты остался жив, но монстр отнимает у тебя ",
                monster_attack,
                " единиц здоровья",
            )
    else:
        print(
            "Сила атаки монстра превосходит твое здоровье, монстр беспощадно тебя убивает..."
        )
        game_over(3)

    random_ch()


def sword_game() -> None:
    """функция описывает действие с мечом."""
    global attack
    print(
        "\nНа миг в твоих глазах помутнело от блеска – перед тобой в воздухе парит новый МЕЧ."
    )
    sword_attack = random.randint(5, 12)
    print("Сила атаки этого меча =", sword_attack)
    print("Чтобы взять меч себе - введи 1, пройти мимо меча - введи 2")

    while True:
        i = int(input())
        if i == 1:
            attack = sword_attack
            print("С новым мечом сила твоей атаки равна ", attack)
            break
        elif i == 2:
            break
        else:
            print(
                "Некорректное значение. Чтобы взять меч себе - введи 1, пройти мимо меча - введи 2."
            )

    random_ch()


def apple_game() -> None:
    """функция описывает действие с яблоком."""
    global hp
    print("\nПо пути ты видишь на полу сочное и спелое яблоко.")
    print(
        "Бежишь к нему, спотыкаясь, чтоб скорее подкрепиться и добавить себе жизненной силы"
    )
    apple_hp = random.randint(3, 10)
    hp = hp + apple_hp
    print("Ты стал мощнее! Сочное яблоко добавляет тебе ", apple_hp, " единиц здоровья")

    random_ch()


def game_over(flag: int) -> int:
    """функция описывает завершение игры."""
    if flag == 1:
        print("Игра завершена. Ты побил всех монстров. ПОБЕДА!!!")
    elif flag == 2:
        print("Игра завершена!")
    elif flag == 3:
        print("Игра завершена. Ты потерпел ПОРАЖЕНИЕ:( ")
    exit()
