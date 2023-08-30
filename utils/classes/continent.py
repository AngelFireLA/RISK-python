#continent class for a RISK strategy game
class Continent:
    def __init__(self, name, bonus_troop_count):
        self.name = name
        self.bonus_troop_count = bonus_troop_count
        self.territories = []

    def is_conquered(self):
        owners = []
        for territory in self.territories:
            if territory.owner not in owners:
                owners.append(territory.owner)
        if len(owners) > 1:
            return False
        return True
