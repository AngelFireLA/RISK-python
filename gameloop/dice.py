from random import randint
from utils.classes.territory import Territory
from gameloop.game import Game


def get_attacking_dices_number(number_of_troops: int) -> int:
    if number_of_troops - 1 >= 3:
        return 3
    elif number_of_troops - 1 <= 0:
        return None
    else:
        return number_of_troops - 1


def get_defending_dices_number(number_of_troops: int) -> int:
    if number_of_troops >= 2:
        return 2
    elif number_of_troops <= 0:
        raise Exception("A territory have no troops")
    else:
        return number_of_troops


def roll_dices(num_dice) -> list:
    return [randint(1, 6) for _ in range(num_dice)]


def battle(attacking_territory: Territory, defending_territory: Territory, game, attacking_troops_amount):
    if game.gamemode == 'normal':
        attacking_troops = attacking_troops_amount
        defending_troops = defending_territory.troops
        while attacking_troops > 0 and defending_troops > 0:
            attacking_dices = roll_dices(get_attacking_dices_number(attacking_troops))
            defending_dices = roll_dices(get_defending_dices_number(defending_troops))
            attacking_dices.sort(reverse=True)
            defending_dices.sort(reverse=True)

            min_dice = min(len(attacking_dices), len(defending_dices))


            for i in range(min_dice):
                if attacking_dices[i] > defending_dices[i]:
                    defending_troops-=1
                else:
                    attacking_troops-=1

        return attacking_troops, defending_troops
    elif game.gamemode == 'simple':
        attacking_troops = attacking_territory.troops-1 - defending_territory.troops
        defending_troops = defending_territory.troops - attacking_territory.troops-1
        if attacking_territory.troops < 1:
            attacking_territory.troops = 1
        elif defending_troops < 0:
            defending_troops = 0

        return attacking_troops, defending_troops
    else:
        raise Exception('Invalid gamemode configured.')

