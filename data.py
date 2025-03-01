import random

from classes import ListHomeInventory, ListPlayerInventoy, SafeMoveItem

home_storage = {
    "weapons": [
        {'broken sword': {"damage": random.randint(15, 20), "attacks_per_turn": 2, "durability": 50}},
        {'regular bow': {"damage": random.randint(10, 15), "attacks_per_turn": 1, "durability": 80}},
        {'magical staff': {"damage": random.randint(25, 30), "attacks_per_turn": 0.5, "durability": 100, "mana_bonus": 20}},
        {'war axe': {"damage": random.randint(30, 40), "attacks_per_turn": 1.5, "durability": 70}},
        {'dagger of shadows': {"damage": random.randint(18, 22), "attacks_per_turn": 3, "durability": 60, "stealth_bonus": 10}}
    ],
    "armor": [
        {'iron helmet': {"defense": 5, "durability": 80}},
        {'leather chestplate': {"defense": 10, "durability": 60}},
        {'steel greaves': {"defense": 8, "durability": 75}},
        {'magical robe': {"defense": 4, "mana_bonus": 30, "durability": 50}}
    ],
    "consumables": [
        {'bread with honey': {"heal": 15, "quantity": 10}},
        {'weak healing potion': {"heal": 25, "quantity": 5}},
        {'resistance potion': {"resistance": 30, "quantity": 3}},
        {'mana potion': {"mana_restore": 50, "quantity": 4}},
        {'elixir of strength': {"strength_bonus": 10, "duration": "5 min", "quantity": 2}}
    ],
    "materials": [
        {'yew wood': {"quantity": 295}},
        {'iron ore': {"quantity": 55}},
        {'copper bar': {"quantity": 12}},
        {'mithril ingot': {"quantity": 5}},
        {'enchanted crystal': {"quantity": 2}}
    ],
    "magical_items": [
        {'ring of wisdom': {"intelligence_bonus": 5, "mana_regen": 10}},
        {'amulet of protection': {"defense_bonus": 8}},
        {'boots of speed': {"speed_bonus": 15}}
    ],
    "quest_items": [
        {'ancient scroll': {"description": "A mysterious scroll with unknown symbols."}},
        {'golden key': {"description": "Opens an ancient treasure chest."}}
    ]
}

# Inventář hráče
player_inventory = {
    "weapons": [
        {'rusty dagger': {"damage": random.randint(5, 10), "attacks_per_turn": 2, "durability": 30}}
    ],
    "armor": [
        {'worn-out leather gloves': {"defense": 2, "durability": 20}}
    ],
    "consumables": [
        {'bread with honey': {"quantity": 2}},
        {'weak healing potion': {"quantity": 1}}
    ]
}

player_backpack = {
    'weapons': [],
    'armor': [],
    'consumables': [],
    "materials": [
        {'iron ore': {"quantity": 20}}
    ],
    "magical_items": [],
    "quest_items": []
}




move_home = SafeMoveItem(player_backpack,home_storage,"iron ore")
move_home.search_category()