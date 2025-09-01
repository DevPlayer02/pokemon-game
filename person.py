import random

from pokemon import *

NAMES = ["Igor", "Joao", "Lorena", "Jhennifer", "Francisco",
         "Diego", "Marcelo", "Mayara", "Gustavo", "Patricia"
]

POKEMONS = [
    FirePokemon("Charmander"),
    FirePokemon("Flarion"),
    FirePokemon("Charmillion"),
    EletricPokemon("Pikachu"),
    EletricPokemon("Raichu"),
    WaterPokemon("Squirtle"),
    WaterPokemon("Magicarp")
]


class Person:

    def __init__(self, name=None, pokemons=[], money=100):
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        self.pokemons = pokemons

        self.money = money

    def __str__(self):
        return self.name

    def show_pokemons(self):
        if self.pokemons:
            print("{}'s pokemons:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} doesn't have any pokemon".format(self))

    def choose_pokemon(self):
        if self.pokemons:
            chosen_pokemon = random.choice(self.pokemons)
            print("{} chose {}".format(self, chosen_pokemon))
            return chosen_pokemon
        else:
            print("ERROR: This player does not have any pokemon")

    def show_wallet(self):
        print("You have ${} in your account".format(self.money))

    def make_money(self, amount):
        self.money += amount
        print("You make ${}".format(amount))
        self.show_wallet()

    def battle(self, person):
        print("{} started a battle with {}".format(self, person))

        person.show_pokemons()
        enemy_pokemon = person.choose_pokemon()

        pokemon = self.choose_pokemon()

        if pokemon and enemy_pokemon:
            while True:
                win = pokemon.attack(enemy_pokemon)
                if win:
                    print("{} winner the battle".format(self))
                    self.make_money(enemy_pokemon.level * 100)
                    break
                enemy_win = enemy_pokemon.attack(pokemon)
                if enemy_win:
                    print("{} winner the battle".format(person))
                    break
        else:
            print("This battle cannot happen")


class Player(Person):
    type = "player"

    def capture(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} captured {}!".format(self, pokemon))

    def choose_pokemon(self):
        self.show_pokemons()

        if self.pokemons:
            while True:
                choice = int(input("Choose your pokemon: "))
                try:
                    choice = int(choice)
                    chosen_pokemon = self.pokemons[choice]
                    print("{} i choose you!!!".format(chosen_pokemon))
                    return chosen_pokemon
                except:
                    print("Invalid choice")
        else:
            print("ERROR: This player does not have any pokemon")

    def explore(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print("A wild pokemon appeared: {}".format(pokemon))

            choice = input("Do you want to capture this pokemon? (s/n):")
            if choice == "s":
                if random.random() >= 0.5:
                    self.capture(pokemon)
                else:
                    print("{} pokemon ran away".format(pokemon))
            else:
                print("Ok, boa viagem")
        else:
            print("No pokemon found during exploration")

class Enemy(Person):
    type = "enemy"

    def __init__(self, name=None, pokemons=None):
        if not pokemons:
            random_pokemons = []
            for i in range(random.randint(1, 6)):
                random_pokemons.append(random.choice(POKEMONS))

            super().__init__(name=name, pokemons=random_pokemons)
        else:
            super().__init__(name=name, pokemons=pokemons)
