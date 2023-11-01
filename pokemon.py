import random
import time
#Background Style
dark_green_background = "\033[42m"
white_text_color = "\033[97m"
print(dark_green_background + white_text_color)
#Pokemon Attributes (Still working on it :) 
class Attributes:
    def __init__(self, defence, attack, speed):
        self.defence = defence
        self.attack = attack
        self.speed = speed
# Here is the main class for type moves etc.
class Pokemon:
    def __init__(self, name, type, level, moves, health):
        self.name = name
        self.type = type
        self.level = level
        self.moves = moves
        self.health = health

# Here are some pokemons
class Charizard(Pokemon):
    def __init__(self):
        super().__init__("Charizard", "Fire", 140, {"Fire Spin": 50, "Flamethrower": 30, "Fly": 60, "Outrage": 90}, 320)

class Mewtwo(Pokemon):
    def __init__(self):
        super().__init__("Mewtwo", "Psychic", 170, {"Psychic": 90, "Shadow Ball": 80, "Aura Sphere": 70, "Recover": 0}, 306)

class Darkrai(Pokemon):
    def __init__(self):
        super().__init__("Darkrai", "Dark", 170, {"Dark Pulse": 80, "Shadow Ball": 80, "Dream Eater": 100, "Nasty Plot": 0}, 306)

class Blastoise(Pokemon):
    def __init__(self):
        super().__init__("Blastoise", "Water", 270, {"Surf": 80, "Hydro Pump": 80, "Hydro Cannon": 100, "Tackle": 40}, 306)

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric", 170, {"Thunderbolt": 80, "1000x Thundervolt": 230, "Volt Tackle": 100, "Thundershock": 40}, 306)
class Venusaur(Pokemon):
    def __init__(self):
        super().__init__("Venusaur", "Grass/Poison", 180, {"Vine Whip": 70, "Solar Beam": 100, "Poison Powder": 0, "Sleep Powder": 0}, 350)

class Gyarados(Pokemon):
    def __init__(self):
        super().__init__("Gyarados", "Water/Flying", 200, {"Aqua Tail": 90, "Dragon Rage": 80, "Hydro Pump": 100, "Bite": 60}, 330)

class Alakazam(Pokemon):
    def __init__(self):
        super().__init__("Alakazam", "Psychic", 160, {"Psychic": 90, "Psybeam": 70, "Reflect": 0, "Recover": 0}, 300)

class Machamp(Pokemon):
    def __init__(self):
        super().__init__("Machamp", "Fighting", 200, {"Karate Chop": 80, "Cross Chop": 100, "Seismic Toss": 75, "Bulk Up": 0}, 360)

class Snorlax(Pokemon):
    def __init__(self):
        super().__init__("Snorlax", "Normal", 220, {"Body Slam": 85, "Hyper Beam": 110, "Rest": 0, "Amnesia": 0}, 400)

class Lapras(Pokemon):
    def __init__(self):
        super().__init__("Lapras", "Water/Ice", 190, {"Ice Beam": 90, "Surf": 80, "Sing": 0, "Confuse Ray": 0}, 340)

class Jolteon(Pokemon):
    def __init__(self):
        super().__init__("Jolteon", "Electric", 160, {"Thunderbolt": 90, "Thunder Wave": 0, "Pin Missile": 75, "Double Kick": 60}, 280)

class Dragonite(Pokemon):
    def __init__(self):
        super().__init__("Dragonite", "Dragon/Flying", 220, {"Dragon Rage": 80, "Dragon Tail": 95, "Fly": 70, "Thunder Wave": 0}, 380)
class Articuno(Pokemon):
    def __init__(self):
        super().__init__("Articuno", "Ice/Flying", 220, {"Ice Beam": 90, "Blizzard": 110, "Roost": 0, "Reflect": 0}, 380)

class Zapdos(Pokemon):
    def __init__(self):
        super().__init__("Zapdos", "Electric/Flying", 220, {"Thunder Shock": 85, "Thunderbolt": 95, "Roost": 0, "Agility": 0}, 380)

class Moltres(Pokemon):
    def __init__(self):
        super().__init__("Moltres", "Fire/Flying", 220, {"Ember": 80, "Flamethrower": 95, "Roost": 0, "Sunny Day": 0}, 380)

class Mew(Pokemon):
    def __init__(self):
        super().__init__("Mew", "Psychic", 250, {"Psychic": 100, "Transform": 0, "Barrier": 0, "Metronome": 0}, 420)

class Raikou(Pokemon):
    def __init__(self):
        super().__init__("Raikou", "Electric", 240, {"Thunderbolt": 95, "Thunder": 110, "Calm Mind": 0, "Roar": 0}, 400)

class Entei(Pokemon):
    def __init__(self):
        super().__init__("Entei", "Fire", 240, {"Ember": 85, "Fire Spin": 100, "Stomp": 0, "Roar": 0}, 400)

class Suicune(Pokemon):
    def __init__(self):
        super().__init__("Suicune", "Water", 240, {"Bubble Beam": 90, "Hydro Pump": 110, "Rain Dance": 0, "Gust": 0}, 400)

class Lugia(Pokemon):
    def __init__(self):
        super().__init__("Lugia", "Psychic/Flying", 280, {"Aero Blast": 110, "Psychic": 100, "Recover": 0, "Safeguard": 0}, 460)

class HoOh(Pokemon):
    def __init__(self):
        super().__init__("Ho-Oh", "Fire/Flying", 280, {"Sacred Fire": 110, "Fire Blast": 100, "Recover": 0, "Sunny Day": 0}, 460)

class Celebi(Pokemon):
    def __init__(self):
        super().__init__("Celebi", "Psychic/Grass", 260, {"Confusion": 90, "Magical Leaf": 95, "Heal Bell": 0, "Safeguard": 0}, 440)
class Goku(Pokemon):
    def __init__(self):
        super().__init__("Goku", "Musa/PlotArmor", 890, {"Kamehamha": 900, "Spirit Bomb": 9995, "KI Blast": 170, "UI": 0}, 940 )
# Create instances of Pokemon

instance_charizard = Charizard()
instance_mewtwo = Mewtwo()
instance_darkrai = Darkrai()
instance_blastoise = Blastoise()
instance_pikachu = Pikachu()
instance_venusaur = Venusaur()
instance_mew = Mew()
instance_celebi = Celebi()
instance_lugia = Blastoise()
instance_hooh = HoOh()
instance_molteres = Moltres()
instance_articuno = Articuno()
instance_zapdos = Zapdos()
instance_entei = Entei()
instance_dragonite = Dragonite()
instance_suicune = Suicune()
instance_machamp = Machamp()
instance_snorlax = Snorlax()
instance_lapras = Lapras()
instance_dragonite = Dragonite()
instance_raikou = Raikou()
instance_gyrados = Gyarados()
instance_jolteaon = Jolteon()
instance_goku = Goku()
#list of python instances

pokemons = [instance_charizard, instance_darkrai, instance_mewtwo,instance_lugia, instance_articuno, instance_celebi, instance_lapras,
            instance_hooh, instance_pikachu, instance_suicune, instance_blastoise, instance_dragonite, instance_entei, instance_gyrados,
            instance_jolteaon, instance_lapras, instance_lugia, instance_zapdos, instance_mew, instance_goku
            ]
# Now, let's randomly choose the computer's Pokemon
comp_pokemon = random.choice(pokemons)
# Ask the user to select their Pokemon
user_pokemon = input("Select Your Pokemon (There are some pokemons that are not currently stored in our database): ").lower()
time.sleep(2)
# Find the user's chosen Pokemon instance
user_pokemon_instance = None
for pokemon in pokemons:
    if user_pokemon == pokemon.name.lower():
        user_pokemon_instance = pokemon
        break
# Check if the user's input corresponds to a valid Pokemon
if user_pokemon_instance:
        print(f"You Chose {user_pokemon_instance.name}")
        print(f"Computer Chose {comp_pokemon.name}")
        print("Your Pokemon's Moves:")
        for move, power in user_pokemon_instance.moves.items():
            print(f"{move}: Power {power}")
else: print("Invalid Pokemon choice. Please select from Charizard, Darkrai, or Mewtwo.")
while user_pokemon_instance.health and comp_pokemon.health > 0:
    #computer move selection
    comp_pokemon_move = random.choice(list(comp_pokemon.moves.keys()))
    #lets battle
    user_move = str(input("Select Your Move the Given Above ")).capitalize()
    if user_move in user_pokemon_instance.moves:
        print(f"You used {user_move}!")
        # Calculate battle result
        user_power = user_pokemon_instance.moves[user_move]
        comp_power = comp_pokemon.moves[comp_pokemon_move]
        if user_power > comp_power:
            comp_pokemon.health -= user_power
            user_pokemon_instance.health -= comp_power
            print(f"You used {user_move} and dealt{user_power}")
            print(comp_pokemon.health)
            print(f"Computer used {comp_pokemon_move} and dealt{comp_power}")
            print(user_pokemon_instance.health)
        elif user_power < comp_power:
            user_pokemon_instance.health -= comp_power
            comp_pokemon.health -= user_power    
            print(f"Computer used {comp_pokemon_move} and dealt{comp_power}")
            print(user_pokemon_instance.health)
            print(f"You used {user_move} and dealt{user_power}")
            print(comp_pokemon.health)
        else:
            print("It's a tie!")
    else:
        print("Invalid move. Please select a valid move from the options.")
# Determine the winner
time.sleep(2)
if user_pokemon_instance.health == 0:
    print("You have run out of power. Computer wins!")
    money = random.randint(20,100)
    print(f"You Lost {money}$")
else:
    print("Congratulations! You defeated the computer!")
    money = random.randint(20,100)
    print(f"You Won {money}$")
