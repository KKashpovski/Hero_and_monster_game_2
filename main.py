"""Python RPG."""


from func import *


def start_game():
    """Запуск игры."""
    ab = Game()
    ab.choose_hero()
    ab.game_play()


start_game()
