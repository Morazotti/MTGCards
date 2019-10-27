class MTGCard:

    def tap_card(self):
            self.tapped = True
            return

    def untap_card(self):
        self.tapped = False
        return
    
    class Creature:
        """A MTG creature class."""
        def __init__(self, name, power, toughness, mana_cost, keywords=[]):
            self.name = name
            self.power = power
            self.toughness = toughness
            self.keywords = keywords
            self.tapped = False
            self.mana_cost = mana_cost
                        
    class Land:
        """A MTG land class."""
        def __init__(self, name, mana, *effects):
            self.mana = mana
            self.effects = effects
            self.tapped = False

    class Enchantment():
        """A MTG enchantment class."""
        def __init__(self, name, is_aura, *effects):
            self.is_aura = is_aura
            self.tapped = False
            self.effects = effects

    class Artifacts:
        """A MTG enchantment class."""
        def __init__(self, name, *effects):
            self.effects = effects
            
    class Instant:
        """A MTG instant class."""
        def __init__(self, name, *effects):
            self.effects = effects

    class Sorcery:
        """A MTG sorcery class."""
        def __init__(self, name, *effects):
            self.effects = effects
            
    def keywords():
        keywords = {
            "Flying": "Flying (This creature can only be blocked by creatures with flying or range.)",
            "Range": "Range (This creature can block creatures with flying.)",
            "Lifelink": "Lifelink (Any damage caused by this creatures gives life to its controller in the same amount caused.)",
            "Deathtouch": "Deathtouch (Any damage caused by this creature to another creature is enough to destroy it.)",
            "Initiative": "Initiative (Any battle damage caused by this creature applies before the damage from other creature.)",
            "Haste": "Haste (This creature can attack the same turn it enters the battlefield.)",
            "Vigilance": "Vigilance (This creature does not tap when self.assertTrue()tacking.)",
            "Hexproof": "Hexproof (This card can not be targeted by any spell or ability from an opponent.)",
            "Shroud": "Shroud (This card can not be targeted by any spell or ability.)",
            "Indestructible": "Indestructible (This card can not be destroyed.)"
        }
        return keywords

kw = MTGCard.keywords()
BASIC_ISLAND = MTGCard.Land(["U"])
BASIC_MOUNTAIN = MTGCard.Land(["R"])
BASIC_PLAINS = MTGCard.Land(["W"])
BASIC_SWAMP = MTGCard.Land(["B"])
BASIC_FOREST = MTGCard.Land(["G"])
LARGE_GOBLIN = MTGCard.Creature("Large goblin",3,2,{"C":2,"R":1},[kw["Haste"], kw["Initiative"]])

deck = {}
deck["BASIC_ISLAND"]=4
deck["LARGE_GOBLIN"]=1
LARGE_GOBLIN.artist = "Karl Korpinski"
LARGE_GOBLIN.keywords.append(kw["Flying"])
print(deck)
