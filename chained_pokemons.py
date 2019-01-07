pokemons = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon \
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite \
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan \
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine \
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 \
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking \
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko \
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

pokemons_list = pokemons.split()


def user_name():
    user = input("Your name: ")
    return user


def get_pokemon_name(user):
    pokemon = input(
        "{} say name of your pokemon: ".format(user.title())).lower()
    return pokemon



def main():
    first_user = user_name()
    second_user = user_name()

    while True:
        while True:
            pokemons_popped = []
            first_pokemon = get_pokemon_name(first_user)
            if first_pokemon in pokemons_list:
                pokemons_popped.append(first_pokemon)
                pokemons_list.remove(first_pokemon)

                second_pokemon = get_pokemon_name(second_user)

                if second_pokemon in pokemons_list and second_pokemon[0] == first_pokemon[-1]:
                    pokemons_popped.append(second_pokemon)
                    pokemons_list.remove(second_pokemon)
                    print()
                    continue
                else:
                    print("\n{} you lose!" .format(second_user.title()))
                    break
            else:
                print("\n{} you lose!".format(first_user.title()))
                break

        repeat_game = input("\nDo you want to play again (y/n)? ")
        if repeat_game == 'y':
            continue
        else:
            break


if __name__ == "__main__":
    main()
