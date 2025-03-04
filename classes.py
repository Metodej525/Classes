from collections import defaultdict



class ListHomeInventory:
    def __init__(self,inventory):
        self.inventory = inventory
    def list_weapons(self):
        print('\n\nWEAPONS\n')
        for category in self.inventory["weapons"]:
            for item_name, stats in category.items():
                print(f'{item_name}:')
                for stat, value in stats.items():
                    print(f'    {stat}:  {value}')
    def list_amor(self):
        print('\n\nARMOR\n')
        for category in self.inventory["armor"]:
            for item_name, stats in category.items():
                print(f'{item_name}:')
                for stat, value in stats.items():
                    print(f'    {stat}:  {value}')
    def list_consumables(self):
        print('\n\nCONSUMABLES\n')
        for category in self.inventory["consumables"]:
            for item_name, stats in category.items():
                print(f'{item_name}:')
                for stat, value in stats.items():
                    print(f'    {stat}:  {value}')
    def list_materials(self):
        print('\n\nMATERIALS\n')
        for category in self.inventory["materials"]:
            for item_name, stats in category.items():
                print(f'{item_name}:')
                for stat, value in stats.items():
                    print(f'    {stat}:  {value}')
    def list_magical_items(self):
        print('\n\nMAGICAL ITEMS\n')
        for category in self.inventory["magical_items"]:
            for item_name, stats in category.items():
                print(f'{item_name}:')
                for stat, value in stats.items():
                    print(f'    {stat}:  {value}')
    def list_quest_items(self):
        print('\n\nQUEST ITEMS\n')
        for category in self.inventory["quest_items"]:
            for item_name, stats in category.items():
                print(f'{item_name}:')
                for stat, value in stats.items():
                    print(f'    {stat}:  {value}')
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
        for category, items in self.inventory.items():
            print(f'\n{category.upper()}:\n')
            for item in items:
                for item_name, stats in item.items():
                    print(f'{item_name}:')
                    for stat, value in stats.items():
                        print(f'    {stat}:  {value}')


    def list_backpack(self):
        """printne backpack"""
        print('\n\nItems in you backpack are:\n')
        for category, items in self.inventory.items():
            print(f'\n{category.upper()}:\n')
            for item in items:
                for item_name, stats in item.items():
                    print(f'{item_name}:')
                    for stat, value in stats.items():
                        print(f'    {stat}:  {value}')
class SafeMoveItem:
    """slouzi k presunuti veci z player inv do home_storage po fightu.... proto Safe...."""
    def __init__(self,source,target,item):
        self.source = source
        self.target = target
        self.item = item
        self.category = None
        self.index = None

    def search_category(self):
        # Prohledáme každou kategorii v source
        for category, items in self.source.items():
            for item_names in items:
                if self.item in item_names:
                    self.category = category
                    return category  # Pokud položka je v jiné kategorii

        # Pokud položka nebyla nalezena ve všech kategoriích
        print('Item not in inventory')
        return None
    def search_index(self):
        for category in self.source[self.category]:
            for items in category:
                if self.item in items:
                    self.index = self.source[self.category].index(category)

            return

    def move(self):
        if self.category is None:
            return
        # Kopie položky, aby pop() neovlivnil její obsah, kdyz je to bez copy tak se ulozi
        # jen odkaz na polozky ve slovniku....
        item_to_move = self.source[self.category][self.index].copy()
        # Odstraníme konkrétní položku ze slovníku
        # pop odstrani key, value, ale vraci jen value.....
        self.source[self.category][self.index].pop(self.item)

        self.target[self.category].append(item_to_move)
        # Pokud je po odstranění slovník prázdný, smažeme ho ze seznamu
        if not self.source[self.category][self.index]:
            del self.source[self.category][self.index]

        print(f'{self.item} moved\n')
class EquipManager:
    def __init__(self,player_inv,backpack,item):
        self.item = item
        self.player_inv = player_inv
        self.backpack= backpack
    def equip(self):
        serch_cat = SafeMoveItem(self.player_inv,self.backpack,self.item)
        serch_cat.search_category()
        serch_cat.search_index()
        serch_cat.move()
    def de_equip(self):
        serch_cat = SafeMoveItem(self.backpack, self.player_inv, self.item)
        serch_cat.search_category()
        serch_cat.search_index()
        serch_cat.move()
class ListStats:
    def __init__(self,target_stats):
        self.target_stats = target_stats
    def list_stats(self):
        for name,stats in self.target_stats.items():
            print(f'\n{name.upper()}')
            for stat_print,value in stats.items():
                print(f'{stat_print}:')
                for stat_name, stat_value in value.items():
                    if stat_print != 'abilities':
                        print(f'    {stat_name}: {stat_value}')
                    else:
                        for ability_name, ability_value in stats['abilities'].items():
                             print(f'    {ability_name}')
class CalcStats:
    """spočítá staty enity + co má na sobě a přičte to """
    def __init__(self, inv, stats):
        self.inv = inv
        self.stats = stats
        self.allowed_stats = {'health', 'armor', 'healing per round', 'attack', 'damage'}  # Seznam statistik, které chceme přičítat

    def calc(self):
        aggregated_stats = defaultdict(int, self.stats['You']['stats'])  # Základní statistiky hráče

        # Sečtení statistik z inventáře
        for items in self.inv.values():
            for item in items:
                for stat in item.values():
                    for stat_name, stat_value in stat.items():
                        if stat_name in self.allowed_stats:  # Přičítáme jen relevantní statistiky
                            aggregated_stats[stat_name] += stat_value

        self.stats['You']['stats'] = dict(aggregated_stats)  # Aktualizace statistik hráče

    def display_stats(self):
        print("Player Stats:")
        for stat_name, stat_value in self.stats['You']['stats'].items():
            print(f"  {stat_name}: {stat_value}")
class Combat:
    def __init__(self, source,target):
        self.source = source
        self.target = target
        self.target_block = False
    def hit(self):
        source_damage = 0
        for name, attributes in self.source.items():
            source_damage = attributes['damage']
            break
        for name, attributes in self.target.items():
            # for atribute_name, stats in atributes.items():
            target_health, target_armor  = attributes['health'], attributes['armor']
            damage_taken = max(0, source_damage - target_armor)
            # Správný výpočet zbývajícího zdraví
            if self.target_block:
                # Pokud cíl blokuje, sníží příchozí poškození na 25%
                attributes['health'] = max(0, round(0.25 * (target_health - damage_taken)))
            else:
                attributes['health'] = max(0, target_health - damage_taken)

            return attributes['health']  # Vrací zdraví prvního zasaženého nepřítele
    def block(self):
        self.target_block = True

class Loot:
    pass
class Vendor:
    pass
class Money:
    pass
class Abilities:
    pass