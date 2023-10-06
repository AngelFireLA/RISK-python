from gameloop.game import Game
from utils.classes.continent import Continent
from utils.classes.player import Player
from utils.classes.territory import Territory

test_territory_1 = Territory("attacking", None, None)
test_territory_2 = Territory("defending", None, None)
test_player = Player("test", "test")
test_player2 = Player("test2", "test2")

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
    Territory("Alaska", "North America", ["Alberta", "Northwest Territory", "Kamchatka"]),
    Territory("Northwest Territory", "North America", ["Alaska", "Alberta", "Greenland", "Ontario"]),
    Territory("Greenland", "North America", ["Northwest Territory", "Ontario", "Quebec", "Iceland"]),
    Territory("Alberta", "North America", ["Alaska", "Northwest Territory", "Ontario"]),
    Territory("Ontario", "North America",
              ["Alberta", "Northwest Territory", "Greenland", "Quebec", "Eastern United States",
               "Western United States"]),
    Territory("Quebec", "North America", ["Greenland", "Ontario", "Eastern United States"]),
    Territory("Western United States", "North America",
              ["Alberta", "Ontario", "Eastern United States", "Central America"]),
    Territory("Eastern United States", "North America",
              ["Ontario", "Quebec", "Western United States", "Central America"]),
    Territory("Central America", "North America", ["Western United States", "Eastern United States", "Venezuela"]),

    # South America
    Territory("Venezuela", "South America", ["Central America", "Peru", "Brazil"]),
    Territory("Peru", "South America", ["Venezuela", "Brazil", "Argentina"]),
    Territory("Brazil", "South America", ["Venezuela", "Peru", "Argentina", "North Africa"]),
    Territory("Argentina", "South America", ["Peru", "Brazil"]),

    # Africa
    Territory("North Africa", "Africa",
              ["Brazil", "Western Europe", "Southern Europe", "Egypt", "East Africa", "Congo"]),
    Territory("Egypt", "Africa", ["North Africa", "East Africa", "Middle East", "Southern Europe"]),
    Territory("East Africa", "Africa", ["Egypt", "North Africa", "Congo", "South Africa", "Madagascar", "Middle East"]),
    Territory("Congo", "Africa", ["North Africa", "East Africa", "South Africa"]),
    Territory("South Africa", "Africa", ["Congo", "East Africa", "Madagascar"]),
    Territory("Madagascar", "Africa", ["South Africa", "East Africa"]),

    # Europe
    Territory("Iceland", "Europe", ["Greenland", "Great Britain", "Scandinavia"]),
    Territory("Scandinavia", "Europe", ["Iceland", "Great Britain", "Ukraine"]),
    Territory("Ukraine", "Europe", ["Scandinavia", "Southern Europe", "Middle East", "Ural", "Afghanistan"]),
    Territory("Great Britain", "Europe", ["Iceland", "Scandinavia", "Northern Europe", "Western Europe"]),
    Territory("Northern Europe", "Europe", ["Great Britain", "Scandinavia", "Ukraine", "Western Europe"]),
    Territory("Southern Europe", "Europe",
              ["Western Europe", "Northern Europe", "Ukraine", "Egypt", "Middle East"]),
    Territory("Western Europe", "Europe",
              ["Great Britain", "Northern Europe", "Southern Europe", "North Africa"]),

    # Oceania (Australia)
    Territory("Indonesia", "Oceania", ["New Guinea", "Western Australia"]),
    Territory("New Guinea", "Oceania", ["Indonesia", "Eastern Australia", "Western Australia"]),
    Territory("Western Australia", "Oceania", ["Indonesia", "New Guinea", "Eastern Australia"]),
    Territory("Eastern Australia", "Oceania", ["New Guinea", "Western Australia"]),

    # Asia
    Territory("Siam", "Asia", ["India", "China", "Indonesia"]),
    Territory("India", "Asia", ["Siam", "China", "Middle East", "Afghanistan"]),
    Territory("China", "Asia", ["Siam", "India", "Mongolia", "Ural", "Siberia"]),
    Territory("Mongolia", "Asia", ["China", "Irkutsk", "Kamchatka", "Japan", "Siberia"]),
    Territory("Japan", "Asia", ["Mongolia", "Kamchatka"]),
    Territory("Irkutsk", "Asia", ["Mongolia", "Kamchatka", "Siberia", "Yakutsk"]),
    Territory("Yakutsk", "Asia", ["Irkutsk", "Kamchatka", "Siberia"]),
    Territory("Kamchatka", "Asia", ["Yakutsk", "Irkutsk", "Mongolia", "Japan", "Alaska"]),
    Territory("Siberia", "Asia", ["China", "Mongolia", "Irkutsk", "Yakutsk", "Ural"]),
    Territory("Afghanistan", "Asia", ["Ukraine", "Ural", "China", "India", "Middle East"]),
    Territory("Ural", "Asia", ["Ukraine", "Afghanistan", "China", "Siberia"]),
    Territory("Middle East", "Asia", ["Ukraine", "Afghanistan", "India", "East Africa", "Southern Europe"]),

]


test_game = Game([test_player, test_player2], 40, territories, continents)
#test_game.run()

# battle = dice.battle(test_territory_1, test_territory_2, test_game)
# print(battle)
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add territories as nodes
for territory in territories:
    G.add_node(territory.name)

# Add edges between connected territories
for territory in territories:
    for neighbor in territory.connected_territories:
        G.add_edge(territory.name, neighbor.name)

# Draw the graph
pos = nx.spring_layout(G, seed=42)

# Draw territories as circles
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue', node_shape='o')

# Draw edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=8)

# Set plot limits
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()


