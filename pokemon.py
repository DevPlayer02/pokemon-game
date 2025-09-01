import random


class Pokemon:

    def __init__(self, species, level=None, name=None):
        self.species = species

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if name:
            self.name = name
        else:
            self.name = species

        self.attack_power = self.level * 5
        self.health = self.level * 10

    def __str__(self):
        return "{} ({}Lvl)".format(self.name, self.level)

    def attack(self, pokemon):
        critical = int((self.attack_power * random.random() * 1.3))
        pokemon.health -= critical
        print("{} it lost {} health points".format(pokemon, critical))

        if pokemon.health <= 0:
            print("{} was defeated".format(pokemon))
            return True
        else:
            return False

class EletricPokemon(Pokemon):
    type = "eletric"

    def attack(self, pokemon):
        print("{} launched a bolt of thunder at {} ".format(self, pokemon))
        return super().attack(pokemon)


class FirePokemon(Pokemon):
    type = "fire"
    def attack(self, pokemon):
        print("{} launched a Fire Ball at {} ".format(self, pokemon))
        return super().attack(pokemon)


class WaterPokemon(Pokemon):
    type = "water"
    def attack(self, pokemon):
        print("{} launched a Water Jet at {} ".format(self, pokemon))
        return super().attack(pokemon)


class Pikachu(EletricPokemon):
    species = "Pikachu"


my_pokemon = EletricPokemon("Pikachu")
friends_pokemon = FirePokemon("Charmander")
