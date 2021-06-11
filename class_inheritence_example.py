

class Player:
    Name = "User provided"
    Health = 100
    Armor = 10

class Fighter(Player)
    Health_modifier = Health * 1.5
    Armor_modifer = Armor * 1.25
    Stamina = 50
    Attack_power = 25

class Wizard(Player)
    Mana = 100
    Spell_power = 40
