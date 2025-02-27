class ListHomeInventory:
    def __init__(self,inventory):
        self.inventory = inventory
    def list_weapons(self):
        print('\n\nWEAPONS\n')
        for category,item_name in self.inventory["weapons"].items():
            print(f'{category}')
            for equip_stat, stats in item_name.items():

                print(f'    {stats}')
    def list_amor(self):
        print('\n\nARMOR\n')
        for category, item_name in self.inventory["armor"].items():
            print(f'{category}')
            for equip_stat, stats in item_name.items():

                print(f'    {stats}')
    def list_consumables(self):
        print('\n\nCONSUMABLES\n')
        for category, item_name in self.inventory["consumables"].items():
            print(f'{category}')
            for equip_stat, stats in item_name.items():

                print(f'    {stats}')
    def list_materials(self):
        print('\n\nMATERIALS\n')
        for category, item_name in self.inventory["materials"].items():
            print(f'{category} \n {item_name}')
    def list_magical_items(self):
        print('\n\nMAGICAL ITEMS\n')
        for category, item_name in self.inventory["magical_items"].items():
            print(f'{category} \n {item_name}')
    def list_quest_items(self):
        print('\n\nQUEST ITEMS\n')
        for category, item_name in self.inventory["quest_items"].items():
            print(f'{category}')
            for equip_stat, stats in item_name.items():

                print(f'    {stats}')
    def list_all(self):
        ListHomeInventory.list_weapons(self)
        ListHomeInventory.list_amor(self)
        ListHomeInventory.list_consumables(self)
        ListHomeInventory.list_materials(self)
        ListHomeInventory.list_magical_items(self)
        ListHomeInventory.list_quest_items(self)
class ListPlayerInventoy:
    def __init__(self,inventory,backpack):
        self.inventory = inventory
        self.backpack = backpack
    def list_equip(self):
        """printne co ma player na sobe"""
        print('Your equipment is :\n')
        for category, item_name in self.inventory.items():
            print(f'\n{category.upper()}\n')
            for name, stats_all in item_name.items():
                for equip_state,stats_item in stats_all.items():
                    print(f'{name}  >>>  {stats_item}')


    def list_backpack(self):
        """printne backpack"""
        print('\n\nItems in you backpack are:\n')
        for category, item in self.backpack.items():
            print(f'\n{category}')
            if self.backpack[category] == {}:
                print('None')
            for item_name , stats in item.items():
                print(f'{item_name} : {stats}')
class SafeMoveItem:
    def __init__(self,source,target,item):
        self.source = source
        self.target = target
        self.item = item
        self.category = None


    def search_category(self):
        # Prohledáme každou kategorii v source
        for category, items in self.source.items():
            if self.item in items:
                self.category = category
                return category  # Pokud položka je v jiné kategorii

        # Pokud položka nebyla nalezena ve všech kategoriích
        print('Item not in inventory')
        return None

    def move(self):
        if self.category is None:
            return
        item_to_move = self.source[self.category].pop(self.item)
        self.target[self.category] = item_to_move
class EquipItem:
    pass
class PlayerStats:
    pass
class EnemyStats:
    pass
class Combat:
    pass
class Loot:
    pass
class Vendor:
    pass
class Money:
    pass