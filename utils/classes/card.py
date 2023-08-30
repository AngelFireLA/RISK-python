#class for a card in the RISK strategy game:
class Card:
    def __init__(self, assigned_territory, assigned_territory_troop_count, owner):
        self.assigned_territory = assigned_territory
        self.assigned_territory_army_count = assigned_territory_troop_count
        self.assigned_owner = owner