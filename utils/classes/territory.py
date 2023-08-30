#Class for a single RISK strategy game territory
class Territory:
    def __init__(self, name, owner, troops, continent, connected_territories):
        self.name = name
        self.owner = owner
        self.troops = troops
        self.continent = continent
        self.connected_territories = connected_territories
        