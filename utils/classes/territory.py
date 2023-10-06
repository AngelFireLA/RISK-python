#Class for a single RISK strategy game territory
class Territory:
    def __init__(self, name, continent, connected_territories):
        self.name = name
        self.owner = None
        self.troops = 1
        self.continent = continent
        self.connected_territories = connected_territories
