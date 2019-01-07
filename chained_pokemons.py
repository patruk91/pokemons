import os
import time


def get_pokemon_list():
    pokemons_list = []
    with open("pokemons.csv") as file_object:
        for line in file_object:
            pokemons_list.append(line.rstrip().lower())
    return pokemons_list


def user_name():
    user = input("Your name: ")
    return user


def get_pokemon_name(user):
    pokemon = input(
        "{} say name of your pokemon: ".format(user.title())).lower()
    return pokemon


def main():
    os.system('clear')
    pokemons_list = get_pokemon_list()

    first_user = user_name()
    second_user = user_name()

    while True:
        while True:
            os.system('clear')
            pokemons_popped = []

            first_pokemon = get_pokemon_name(first_user)
            if first_pokemon in pokemons_list:
                pokemons_popped.append(first_pokemon)
                pokemons_list.remove(first_pokemon)

                second_pokemon = get_pokemon_name(second_user)

                if second_pokemon in pokemons_list and second_pokemon[0] == first_pokemon[-1]:
                    pokemons_popped.append(second_pokemon)
                    pokemons_list.remove(second_pokemon)
                    print("\nGOOD ANSWER!")
                    time.sleep(3)

                    continue
                else:
                    print("\n{} you lose!" .format(second_user.title()))
                    break
            else:
                print("\n{} you lose!".format(first_user.title()))
                break

        repeat_game = input("\nDo you want to play again (y/n)? ")
        if repeat_game == 'y':
            print()
            continue
        else:
            break


if __name__ == "__main__":
    main()
