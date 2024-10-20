import pickle

from pokemon import *
from person import *


def choose_starter_pokemon(player):
    print("Hello {}, You can now choose the pokemon that will accompany you on this journey!".format(player))

    pikachu = EletricPokemon("Pikachu", level=1)
    charmander = FirePokemon("Charmander", level=1)
    squirtle = WaterPokemon("Squirtle", level=1)

    print("You have 3 choices: ")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        choice = input("Choose your pokemon: ")

        if choice == "1":
            player.capture(pikachu)
            break
        elif choice == "2":
            player.capture(charmander)
            break
        elif choice == "3":
            player.capture(squirtle)
            break
        else:
            print("Invalid choice")


def save_game(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Game saved successfully")
    except Exception as error:
        print("Error saving game")
        print(error)


def load_game():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Game loaded successfully")
            return player
            print("Game saved successfully")
    except Exception as error:
        print("Archive not found")
        print(error)


if __name__ == "__main__":
    print("_______________________________________________________________________________________________________")
    print("Welcome to the terminal pokemon RPG game")
    print("_______________________________________________________________________________________________________")

    player = load_game()

    if not player:
        name = input("Hello, what's your name: ")
        player = Player(name)
        print("Hello {}, this is a world inhabited by pokemons,"
              " from now on your mission is to become a pokemon trainer".format(player))
        print("Capture as many pokemon as you can and defeat your enemies")
        player.show_wallet()

        if player.pokemons:
            print("I saw that you have some pokemons")
            player.show_pokemons()
        else:
            print("You don't have any pokemon")
            choose_starter_pokemon(player)

        print("Now that you already have a Pokemon, face your arch-rival from kindergarten")
        gary = Enemy(name="Gary", pokemons=[WaterPokemon("Squirtle", level=1)])
        player.battle(gary)
        save_game(player)

    while True:
        print("_______________________________________________________________________________________________________")
        print("What do you want to do ?")
        print("1 - Explore the Pokemon world")
        print("2 - Fight with an enemy")
        print("3 - See Pokeagenda")
        print("0 - Leave the game")
        choice = input("Your choice: ")

        if choice == "0":
            print("Bye bye!!")
            break
        elif choice == "1":
            player.explore()
            save_game(player)
        elif choice == "2":
            random_enemy = Enemy()
            player.battle(random_enemy)
            save_game(player)
        elif choice == "3":
            player.show_pokemons()
        else:
            print("Invalid choice")