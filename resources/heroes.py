
# List of heroes
heroes = [                                                     
    "Abaddon",                                                     # strenght 
    "Alchemist",	
    "Axe",
    "Beastmaster",	
    "Brewmaster",
    "Bristleback",
    "Centaur Warrunner",
    "Chaos Knight",
    "Clockwerk",
    "Doom",
    "Dragon Knight",
    "Earth Spirit",
    "Earthshaker",
    "Elder Titan",
    "Huskar",
    "Io",
    "Kunkka",
    "Legion Commander",
    "Lifestealer",
    "Lycan",
    "Magnus",
    "Night Stalker",
    "Omniknight",
    "Phoenix",	
    "Pudge",
    "Sand King",
    "Slardar",
    "Spirit Breaker",
    "Sven",
    "Tidehunter",
    "Timbersaw",
    "Tiny",
    "Treant Protector",
    "Tusk",
    "Underlord",
    "Undying",
    "Wraith King",
    "Anti-Mage",                                                   # agility
    "Arc Warden",
    "Bloodseeker",
    "Bounty Hunter",
    "Broodmother",
    "Clinkz",
    "Drow Ranger",
    "Ember Spirit",
    "Faceless Void",
    "Gyrocopter",
    "Juggernaut",
    "Lone Druid",
    "Luna",
    "Medusa",
    "Meepo",
    "Mirana",
    "Monkey King",
    "Morphling",
    "Naga Siren",
    "Nyx Assassin",
    "Pangolier",
    "Phantom Assassin",
    "Phantom Lancer",
    "Razor",
    "Riki",
    "Shadow Fiend",
    "Slark",
    "Sniper",
    "Spectre",
    "Templar Assassin",
    "Terrorblade",
    "Troll Warlord",
    "Ursa",
    "Vengeful Spirit",
    "Venomancer",
    "Viper",
    "Weaver",
    "Ancient Apparition",                                           # intelligence
    "Bane",
    "Batrider",
    "Chen",
    "Crystal Maiden",
    "Dark Seer",
    "Dark Willow",
    "Dazzle",
    "Death Prophet",
    "Disruptor",
    "Enchantress",
    "Enigma",
    "Invoker",
    "Jakiro",
    "Keeper of the Light", 
    "Leshrac",
    "Lich",
    "Lina",
    "Lion",
    "Nature’s Prophet",
    "Necrophos",
    "Ogre Magi",
    "Oracle",
    "Outworld Devourer",
    "Puck",
    "Pugna",
    "Queen of Pain",
    "Rubick",
    "Shadow Demon",
    "Shadow Shaman",
    "Silencer",
    "Skywrath Mage",
    "Storm Spirit",
    "Techies",
    "Tinker",
    "Visage",
    "Warlock",
    "Windranger",
    "Winter Wyvern",
    "Witch Doctor",
    "Zeus",                                                                      
]  


structuredHeroes = {
    'pos1' : [
        "Slark",
        "Spectre",
        "Wraith King",
    ],


    'pos2' : [
        "Storm Spirit",
        "Lina",
        "Puck",
    ],


    'pos3' : [
        "Axe",
        "Bristleback",
        "Beastmaster",
    ],


    'pos4' : [
        "Mirana",
        "Jakiro",
        "Dark Willow",
    ],


    'pos5' : [
        "Oracle",
        "Witch Doctor",
        "Dazzle"
    ]
}


# flatten dictionary
def flatten(structured):

    flat = []

    for key in structured.keys():
        flat = flat + structured[key]
    
    return flat

# flat list of all heroes
heroes = flatten(structuredHeroes)