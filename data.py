import random

from classes import Combat, ListStats, CalcStats

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
        {'worn-out leather gloves': {"armor": 2, "durability": 20}}
    ],
    "consumables": [
        {'bread with honey': {"quantity": 2}},
        {'weak healing potion': {"quantity": 1}}
    ]
}

player_backpack = {
    'weapons': [
        {'rusty dagger': {"damage": random.randint(5, 10), "attacks_per_turn": 2, "durability": 30}},
        {'rusty dagger': {"damage": random.randint(5, 10), "attacks_per_turn": 2, "durability": 30}},
        {'magical staff': {"damage": random.randint(25, 30), "attacks_per_turn": 0.5, "durability": 100, "mana_bonus": 20}}],
    'armor': [],
    'consumables': [],
    "materials": [
        {'iron ore': {"quantity": 20}}
    ],
    "magical_items": [],
    "quest_items": []
}

player_stats = {
    'You':{
        'stats':{'health':100,'armor':5,'healing per round':2,'damage':20},
        'abilities':{}}}

weak_enemy = {
    "slime": {
        "stats": {"health": 30, "armor": 0, "healing per round": 1, "damage": 5},
        "abilities": {"split": {"type": "passive", "effect": "duplicates on death"}}
    },
    "goblin": {
        "stats": {"health": 50, "armor": 5, "healing per round": 2, "damage": 10},
        "abilities": {"quick strike": {"type": "damage", "power": 15}}
    },
    "giant_rat": {
        "stats": {"health": 40, "armor": 2, "healing per round": 1, "damage": 7},
        "abilities": {"infectious bite": {"type": "damage", "power": 10, "effect": "poison"}}
    }
}

medium_enemy = {
    "skeleton_warrior": {
        "stats": {"health": 80, "armor": 10, "healing per round": 0, "damage": 15},
        "abilities": {"bone_shield": {"type": "buff", "power": 10}}
    },
    "orc_grunt": {
        "stats": {"health": 120, "armor": 15, "healing per round": 3, "damage": 20},
        "abilities": {"rage": {"type": "buff", "power": 10, "effect": "increased attack for 3 rounds"}}
    },
    "shadow_assassin": {
        "stats": {"health": 70, "armor": 5, "healing per round": 0, "damage": 25},
        "abilities": {"shadow_step": {"type": "evasion", "effect": "dodges next attack"}}
    }
}

strong_enemy = {
    "fire_elemental": {
        "stats": {"health": 150, "armor": 20, "healing per round": 5, "damage": 30},
        "abilities": {"flame_burst": {"type": "damage", "power": 40, "effect": "burn"}}
    },
    "stone_golem": {
        "stats": {"health": 200, "armor": 50, "healing per round": 2, "damage": 20},
        "abilities": {"earthquake": {"type": "damage", "power": 50, "effect": "stuns target"}}
    },
    "vampire_lord": {
        "stats": {"health": 180, "armor": 15, "healing per round": 10, "damage": 25},
        "abilities": {"life_drain": {"type": "heal", "power": 20, "effect": "heals for damage dealt"}}
    }
}

encounter = {"slime": {
        "stats": {"health": 30, "armor": 0, "healing per round": 1, "damage": 5},
        "abilities": {"split": {"type": "passive", "effect": "duplicates on death"}}
    }}
calc = CalcStats(player_inventory,player_stats)
calc.calc()
calc.display_stats()
attack_p = Combat(player_stats['You'],encounter['slime'])
attack_p.hit()
list_enemy_stats = ListStats(encounter)
list_enemy_stats.list_stats()
