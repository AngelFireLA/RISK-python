from random import randint
from random import shuffle
from utils.classes.card import Card
from math import floor
import utils.general_functions


class Game:
    phase_list = ["distribution", "attacking", "fortification"]
    card_categories = ['soldier', 'artillery', 'cavalry']

    def __init__(self, players, initial_troop_count, territories: list, continents: list, mode="normal"):
        self.gamemode = mode
        self.players = players
        self.turn_count = 1
        self.game_phase = self.phase_list[0]
        self.all_remaining_cards = []
        self.initial_troop_count = initial_troop_count
        self.territories = territories
        self.continents = continents
        self.card_exchange_multiplier = 1
        self.game_running = False
        self.setup()

    def setup(self):
        for player in self.players:
            player.game = self
        self.link_territories_and_continents()
        if len(self.territories) % len(self.players) != 0:
            raise Exception("Number of territories must be divisible by the number of players")
        self.generate_cards()
        self.distribute_troops()

    # main gameloop
    def run(self):
        self.game_running = True
        # a loop for a game
        # and inside a loop for a turn
        # reminder : if battle is won, draw card, but if more than 5 then force trade and go back to early phase
        for player in self.players:
            player.remaining_troops = floor(len(player.territories)/3)
            if player.remaining_troops < 3:
                player.remaining_troops = 3

        while self.game_running:

            player = self.players[self.turn_count % len(self.players)]

            for continent in self.continents:
                continent_owner = continent.is_conquered()
                if continent_owner and continent_owner == player:
                    player.remaining_troops += continent.bonus_troop_count
                    print("For having fully conquered ", continent.name, ", you gained ", continent.bonus_troop_count, " troops")


            while player.remaining_troops > 0:
                print("Your current territories are :")
                for territory in player.territories:
                    print(territory.name, end=', ')
                print()
                selected_territory = input("Select a territory to distribute troops : ")
                territory = [territory for territory in player.territories if territory.name == selected_territory]
                while not territory:
                    print("Invalid territory")
                    selected_territory = input("Select a territory to distribute troops : ")
                    territory = [territory.name for territory in player.territories if
                                 territory.name == selected_territory]

                territory = territory[0]

                print("You have selected ", selected_territory, "that holds ", territory.troops, " troops")
                print()
                print("You have ", player.remaining_troops, " troops remaining")
                number_of_troops_to_distribute = input("How many troops do you want to distribute ? ")
                #ask until entered value is a valid number and that the number is inferior or equal to the remaining troops of the player
                while not number_of_troops_to_distribute.isnumeric() or int(number_of_troops_to_distribute) > player.remaining_troops:
                    print("Invalid number")
                    number_of_troops_to_distribute = input("How many troops do you want to distribute ? ")

                territory.troops+=int(number_of_troops_to_distribute)
                player.remaining_troops-=int(number_of_troops_to_distribute)
                print("You have added ", number_of_troops_to_distribute, " troops to ", territory.name, "which now currently holds ", territory.troops, " troops")

            print("You have added all your troops to your territories")
            self.game_phase = self.phase_list[1]
            print()
            print("Entering attack phase..." )

            while self.game_phase == self.phase_list[1]:
                print("Your current territories are :")
                for t in player.territories:
                    print(t.name, end=', ')
                print()
                selected_territory = input("Select a territory to attack from : ")
                territory = [territory for territory in player.territories if territory.name == selected_territory]
                while not territory:
                    print("Invalid territory")
                    selected_territory = input("Select a territory to attack from : ")
                    territory = [territory for territory in player.territories if territory.name == selected_territory]

                territory = territory[0]

                print("You have selected ", selected_territory, "that holds ", territory.troops, " troops")
                print()
                print("Your current territories attackable territories are :")
                for t in player.get_attackable_territories(selected_territory):
                    print(t.name, end=', ')
                print()
                territory_to_attack_name = input("Select a territory to distribute troops : ")
                territory_to_attack = [territory for territory in player.territories if territory.name == territory_to_attack_name]
                while not territory_to_attack:
                    print("Invalid territory")
                    territory_to_attack_name = input("Select a territory to distribute troops : ")
                    territory_to_attack = [territory for territory in player.territories if
                                           territory.name == territory_to_attack_name]

                territory_to_attack = territory_to_attack[0]

                print("You have selected ", territory_to_attack, "to attack whi have ", territory_to_attack.troops, " troops")

                number_of_troops_to_distribute = input("How many troops do you want to attack with ? ")
                # ask until entered value is a valid number and that the number is inferior or equal to the remaining troops of the player
                while not number_of_troops_to_distribute.isnumeric() or int(
                        number_of_troops_to_distribute) > territory.troops-1:
                    print("Invalid number")
                    number_of_troops_to_distribute = input("How many troops do you want to distribute ? ")

                territory.troops += int(number_of_troops_to_distribute)
                player.remaining_troops -= int(number_of_troops_to_distribute)
                print("You have added ", number_of_troops_to_distribute, " troops to ", territory.name,
                      "which now currently holds ", territory.troops, " troops")

            self.turn_count += 1

    # generate the list of cards
    def generate_cards(self):
        cards_by_type = {category: len(self.territories) // 3 + (1 if i < len(self.territories) % 3 else 0) for
                         i, category in enumerate(self.card_categories)}

        for territory in self.territories:
            for category in self.card_categories:
                if cards_by_type[category]:
                    self.all_remaining_cards.append(Card(territory, randint(1, 3), category))
                    cards_by_type[category] -= 1
                    break

    # distribute the troops to the territories and the players
    def distribute_troops(self):
        if not len(self.territories) % len(self.players) == 0:
            raise Exception("Number of territories must be divisible by the number of players")
        territories_to_distribute = self.territories
        shuffle(territories_to_distribute)
        territory_per_person = len(self.territories) // len(self.players)
        territory_index = 0
        for player in self.players:
            for j in range(territory_per_person):
                player.territories.append(territories_to_distribute[territory_index])
                territories_to_distribute[territory_index].owner = player
                territory_index += 1
            for k in range(self.initial_troop_count-territory_per_person):
                #get a random territory of the player
                random_territory = player.territories[randint(0, len(player.territories) - 1)]
                random_territory.troops+=1



    # exchange 3 cards for X amount of troops
    def trade_cards(self, player):
        if len(player.cards) < 3:
            raise Exception("Not enough cards to trade")
        if self.gamemode == "normal":
            card_types = {'soldier': 0, 'artillery': 0, 'cavalry': 0}
            soldiers = []
            artillery = []
            cavalry = []
            for card in player.cards:
                if card.category == 'soldier':
                    soldiers.append(card)
                    card_types['soldier'] += 1
                if card.category == 'artillery':
                    artillery.append(card)
                    card_types['artillery'] += 1
                if card.category == 'cavalry':
                    cavalry.append(card)
                    card_types['cavalry'] += 1
            if card_types['soldier'] > 1 and card_types['artillery'] > 1 and card_types['cavalry'] > 1:
                player.remaining_troops += 5 * self.card_exchange_multiplier
                self.card_exchange_multiplier += 1
                player.cards.remove(soldiers[0])
                player.cards.remove(artillery[0])
                player.cards.remove(cavalry[0])
                return True
            if card_types['soldier'] > 3:
                player.remaining_troops += 5 * self.card_exchange_multiplier
                self.card_exchange_multiplier += 1
                for i in range(3):
                    player.cards.remove(soldiers[i])
                return True
            if card_types['artillery'] > 3:
                player.remaining_troops += 5 * self.card_exchange_multiplier
                self.card_exchange_multiplier += 1
                for i in range(3):
                    player.cards.remove(artillery[i])
                return True
            if card_types['cavalry'] > 3:
                player.remaining_troops += 5 * self.card_exchange_multiplier
                self.card_exchange_multiplier += 1
                for i in range(3):
                    player.cards.remove(cavalry[i])
                return True
        if self.gamemode == "simple":
            player.remaining_troops += 10
            for i in range(3):
                player.cards.pop()
            return True

    def draw_card(self):
        # gets random card, remove it from deck, then return the card
        card = self.all_remaining_cards[randint(0, len(self.all_remaining_cards) - 1)]
        self.all_remaining_cards.remove(card)
        return card

    def get_territory_by_name(self, name):
        for territory in self.territories:
            if territory.name == name:
                return territory

    def get_continent_by_name(self, name):
        for continent in self.continents:
            if continent.name == name:
                return continent

    def link_territories_and_continents(self):
        for territory in self.territories:

            # Make sure the owner of the territory has it in his list of territories
            if territory.owner:
                territory.owner.territories.append(territory)

            # Make sure the territory has an instance of a continent as a continent (instead of just a string)
            # and make sure the continent has the territory in it's list of territories
            for continent in self.continents:
                if continent.name == territory.continent:
                    territory.continent = continent
                    continent.territories.append(territory)

            #Make the conncted territories type in the list from str to territory
            neighbors = []
            for neighbor in territory.connected_territories:
                for territory_bis in self.territories:
                    if territory_bis.name == neighbor:
                        neighbors.append(territory_bis)
            territory.connected_territories = neighbors
