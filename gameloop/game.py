from random import randint
class Game:

    def __init__(self, players, initial_troop_count, territories:list, continents:list, mode="normal"):
        self.gamemode = mode
        self.players = players
        self.turn_count = 1
        self.game_phase = None
        self.all_remaining_cards = []
        self.initial_troop_count = initial_troop_count
        self.territories = territories
        self.continents = continents
        self.setup()


    def setup(self):
        for player in self.players:
            player.game = self
        self.link_territories_and_continents()
        if len(self.territories) % len(self.players) != 0:
            raise Exception("Number of territories must be divisible by the number of players")

    #main gameloop
    def run(self):
        pass

    #generate the list of cards
    def generate_cards(self):
        pass

    #distribute the troops to the territories and the players
    def distribute_troops(self):
        pass

    #exchange 3 cards for X amount of troops
    def trade_cards(self):
        pass

    def draw_card(self):
        #gets random card, remove it from deck, then return the card
        card = self.all_remaining_cards[randint(0, len(self.all_remaining_cards)-1)]
        self.all_remaining_cards.remove(card)
        return card

    def get_territory_by_name(self, name):
        for continent in self.continents:
            for territory in continent.territories:
                if territory.name == name:
                    return territory



