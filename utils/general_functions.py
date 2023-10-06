def is_territory_in_list(territory_name, territory_list):
    for territory in territory_list:
        if territory_name == territory.name:
            return True
    return False