"""Python RPG."""


from func import *


def start_game():
    """Пока игрок не введет 0, чтобы остановить игру, продолжайте игру."""
    while True:
        # функция - введение в игру и выбор персонажа.
        ab = Game()
        ab.choose_hero()

        # функция запускает основной игровой цикл.
        ab.game_play()

        print('\t Хочешь сыграть снова?')
        print('\t Введи [1] --> ДА, погнали!')
        print('\t Введи [0] --> Нет, на сегодня хватит!')

        play_again = int(input('\t Опция: '))

        if play_again == 1:
            continue
        else:
            break

    print('\n\n\t Пока:) Возвращайся позже! :D\n\n')


start_game()
