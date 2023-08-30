from gameloop.game import Game
from utils.classes.territory import Territory
from utils.classes.continent import Continent

from utils.classes.player import Player
import gameloop.dice as dice

test_territory_1 = Territory("attacking", 'test', 4, None, None)
test_territory_2 = Territory("defending", 'test', 100, None, None)
test_player = Player("test", "test")

continents = [
    Continent("North America", 5),
    Continent("South America", 2),
    Continent("Europe", 5),
    Continent("Africa", 3),
    Continent("Asia", 7),
    Continent("Oceania", 2)
]

# Creating instances of territories for each continent
territories = [
    # North America
    Territory("Alaska", test_player, 1, "North America", ["Alberta", "Northwest Territory", "Kamchatka"]),
    Territory("Northwest Territory", test_player, 1, "North America", ["Alaska", "Alberta", "Greenland", "Ontario"]),
    Territory("Greenland", test_player, 1, "North America", ["Northwest Territory", "Ontario", "Quebec", "Iceland"]),
    Territory("Alberta", test_player, 1, "North America", ["Alaska", "Northwest Territory", "Ontario"]),
    Territory("Ontario", test_player, 1, "North America", ["Alberta", "Northwest Territory", "Greenland", "Quebec", "Eastern United States", "Western United States"]),
    Territory("Quebec", test_player, 1, "North America", ["Greenland", "Ontario", "Eastern United States"]),
    Territory("Western United States", test_player, 1, "North America", ["Alberta", "Ontario", "Eastern United States", "Central America"]),
    Territory("Eastern United States", test_player, 1, "North America", ["Ontario", "Quebec", "Western United States", "Central America"]),
    Territory("Central America", test_player, 1, "North America", ["Western United States", "Eastern United States", "Venezuela"]),

    # South America
    Territory("Venezuela", test_player, 1, "South America", ["Central America", "Peru", "Brazil"]),
    Territory("Peru", test_player, 1, "South America", ["Venezuela", "Brazil", "Argentina"]),
    Territory("Brazil", test_player, 1, "South America", ["Venezuela", "Peru", "Argentina", "North Africa"]),
    Territory("Argentina", test_player, 1, "South America", ["Peru", "Brazil"]),

    # Africa
    Territory("North Africa", test_player, 1, "Africa", ["Brazil", "Western Europe", "Southern Europe", "Egypt", "East Africa", "Congo"]),
    Territory("Egypt", test_player, 1, "Africa", ["North Africa", "East Africa", "Middle East", "Southern Europe"]),
    Territory("East Africa", test_player, 1, "Africa", ["Egypt", "North Africa", "Congo", "South Africa", "Madagascar", "Middle East"]),
    Territory("Congo", test_player, 1, "Africa", ["North Africa", "East Africa", "South Africa"]),
    Territory("South Africa", test_player, 1, "Africa", ["Congo", "East Africa", "Madagascar"]),
    Territory("Madagascar", test_player, 1, "Africa", ["South Africa", "East Africa"]),

    # Europe
    Territory("Iceland", test_player, 1, "Europe", ["Greenland", "Great Britain", "Scandinavia"]),
    Territory("Scandinavia", test_player, 1, "Europe", ["Iceland", "Great Britain", "Ukraine"]),
    Territory("Ukraine", test_player, 1, "Europe", ["Scandinavia", "Southern Europe", "Middle East", "Ural", "Afghanistan"]),
    Territory("Great Britain", test_player, 1, "Europe", ["Iceland", "Scandinavia", "Northern Europe", "Western Europe"]),
    Territory("Northern Europe", test_player, 1, "Europe", ["Great Britain", "Scandinavia", "Ukraine", "Western Europe"]),
    Territory("Southern Europe", test_player, 1, "Europe",
              ["Western Europe", "Northern Europe", "Ukraine", "Egypt", "Middle East"]),
    Territory("Western Europe", test_player, 1, "Europe",
              ["Great Britain", "Northern Europe", "Southern Europe", "North Africa"]),

    # Oceania (Australia)
    Territory("Indonesia", test_player, 1, "Oceania", ["New Guinea", "Western Australia"]),
    Territory("New Guinea", test_player, 1, "Oceania", ["Indonesia", "Eastern Australia", "Western Australia"]),
    Territory("Western Australia", test_player, 1, "Oceania", ["Indonesia", "New Guinea", "Eastern Australia"]),
    Territory("Eastern Australia", test_player, 1, "Oceania", ["New Guinea", "Western Australia"]),

    # Asia
    Territory("Siam", test_player, 1, "Asia", ["India", "China", "Indonesia"]),
    Territory("India", test_player, 1, "Asia", ["Siam", "China", "Middle East", "Afghanistan"]),
    Territory("China", test_player, 1, "Asia", ["Siam", "India", "Mongolia", "Ural", "Siberia"]),
    Territory("Mongolia", test_player, 1, "Asia", ["China", "Irkutsk", "Kamchatka", "Japan", "Siberia"]),
    Territory("Japan", test_player, 1, "Asia", ["Mongolia", "Kamchatka"]),
    Territory("Irkutsk", test_player, 1, "Asia", ["Mongolia", "Kamchatka", "Siberia", "Yakutsk"]),
    Territory("Yakutsk", test_player, 1, "Asia", ["Irkutsk", "Kamchatka", "Siberia"]),
    Territory("Kamchatka", test_player, 1, "Asia", ["Yakutsk", "Irkutsk", "Mongolia", "Japan", "Alaska"]),
    Territory("Siberia", test_player, 1, "Asia", ["China", "Mongolia", "Irkutsk", "Yakutsk", "Ural"]),
    Territory("Afghanistan", test_player, 1, "Asia", ["Ukraine", "Ural", "China", "India", "Middle East"]),
    Territory("Ural", test_player, 1, "Asia", ["Ukraine", "Afghanistan", "China", "Siberia"]),
    Territory("Middle East", test_player, 1, "Asia", ["Ukraine", "Afghanistan", "India", "East Africa", "Southern Europe"]),

]


test_game = Game([test_player], 1, territories, continents)

# battle = dice.battle(test_territory_1, test_territory_2, test_game)
# print(battle)


source_territory = test_game.get_territory_by_name("Test")
target_territory = territories[5]  # Target Territory instance






