import os
import random
from twitchio.ext import commands

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.command(name='test')                                             
async def test(ctx):
    await ctx.send('Funguje to')

@bot.command(name='tina')                                              
async def tina(ctx):
    await ctx.send('jsem tina, je mi 17 a uz 4 roky piju kavu')       


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


picked = [


]

def selectHero():
    return random.choice(heroes)


@bot.command(name='pick')                                             
async def pick(ctx):
    selected = selectHero()    
    await ctx.send(selected)
    picked.append(selected)


if __name__ == "__main__":
    bot.run()

