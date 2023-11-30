import random
import time
from Pokemon import Pokemon

def setBackgroundStyle() -> None:
    """
    Sets a dark green background with white text color
    """
    dark_green_background = "\033[42m"
    white_text_color = "\033[97m"
    print(dark_green_background + white_text_color)

def makeMoveDictionary(filename: str) -> dict:
    """
    Reads the filename and creates a dict of the form:
        move_name: move_power
    """
    infile = open(filename, "r")
    contents = infile.readlines()
    infile.close()

    moves = dict()
    for line in contents:
        line = line.split(",")
        name = line[0]
        power = int(line[1])

        moves[name] = power

    return moves

def makePokemon(pokemonFile: str, movesFile: str) -> list:
    """
    Reads the pokemonFile and creates a list of Pokemon
    using the movesFile to populate their moves
    """
    moves = makeMoveDictionary(movesFile)

    infile = open(pokemonFile, "r")
    contents = infile.readlines()
    infile.close()

    pokemons = []

    for line in contents:
        line = line.split(",")
        name = line[0]
        types = line[1]
        level = int(line[2])
        pokemonMoves = [line[3], line[4], line[5], line[6]]
        health = int(line[7])

        pokemonMovesDict = dict()
        for pokemonMove in pokemonMoves:
            pokemonMovesDict[pokemonMove] = moves[pokemonMove]

        pokemon = Pokemon(name, types, level, pokemonMovesDict, health)
        pokemons.append(pokemon)

    return pokemons

if __name__ == "__main__":
    pokemons = makePokemon("pokemon.csv", "moves.csv")

    # Set background style
    setBackgroundStyle()
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
