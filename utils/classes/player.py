import gameloop.dice as dice
import utils.classes.territory as Territory
from gameloop.game import Game


class Player:
    def __init__(self, name, color):
        self.territories = []
        self.name = name
        self.color = color
        self.cards = []
        self.game: Game = None

    def get_total_troop_count(self):
        total_troop_count = 0
        for territory in self.territories:
            total_troop_count += territory.troop_count
        return total_troop_count

    # attack a territory with one territory
    def attack(self, own_territory: Territory, opponent_territory: Territory, attacking_troops_amount):
        if not own_territory in self.territories:
            raise Exception("Player does not own this territory")
        if not opponent_territory.name in own_territory.connected_territories:
            raise Exception("Territories are not connected")
        if self.game.gamemode == "normal":
            if own_territory.troop_count - attacking_troops_amount < 1:
                raise Exception("Not enough troops to attack")
        if self.game.gamemode == "simple":
            if own_territory.troop_count < 2:
                raise Exception("Not enough troops to attack")
        resulting_attacking_troops, resulting_defending_troops = dice.battle(own_territory, opponent_territory,
                                                                             self.game, attacking_troops_amount)

        if resulting_defending_troops <= 0:
            opponent_territory.owner.territories.remove(opponent_territory)
            opponent_territory.owner = self
            opponent_territory.troop_count = resulting_attacking_troops
            if self.game.gamemode == "normal":
                own_territory.troop_count -= resulting_attacking_troops
                return True
            if self.game.gamemode == "simple":
                own_territory.troop_count = 1
                return True
        else:
            opponent_territory.troop_count = resulting_defending_troops
            own_territory.troop_count = 1
            return False


    # distribute X amount of troops to a territory
    def reinforce(self, territory, amount_of_troops):
        if not territory in self.territories:
            raise Exception("Player does not own this territory")
        territory.troop_count += amount_of_troops

    # move X amount of troops from one territory to another if they are connected
    def fortify(self, original_territory, new_territory, amount_of_troops):
        if not original_territory in self.territories:
            raise Exception("Player does not own this territory")
        if not new_territory in self.territories:
            raise Exception("Player does not own this territory")
        if not original_territory.name in original_territory.connected_territories:
            raise Exception("Territories are not connected")
        if original_territory.troop_count < amount_of_troops + 1:
            raise Exception("Not enough troops to move")
        territories_are_connected = self.is_indirectly_connected(self.game.territories,
                                                                 self.game.territories.index(original_territory),
                                                                 self.game.territories.index(new_territory))

        if territories_are_connected:
            original_territory.troop_count -= amount_of_troops
            new_territory.troop_count += amount_of_troops

    def is_indirectly_connected(self, source, target, visited=None):
        if visited is None:
            visited = set()

        if source == target:
            return True

        visited.add(source)

        for connected_territory in self.game.territories[source].connected_territories:
            connected_territory_index = self.game.territories.index(connected_territory)
            if connected_territory_index not in visited and connected_territory.owner == self.game.territories[
                source].owner:
                if self.is_indirectly_connected(connected_territory_index, target, visited):
                    return True

        return False
