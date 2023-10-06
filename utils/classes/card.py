#class for a card in the RISK strategy game:
class Card:
    def __init__(self, assigned_territory, assigned_territory_troop_count, category=None):
        self.assigned_territory = assigned_territory
        self.assigned_territory_army_count = assigned_territory_troop_count
        self.assigned_owner = None
        self.category = category