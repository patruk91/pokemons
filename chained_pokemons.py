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




def main():
    first_user = user_name()
    second_user = user_name()

    first_pokemon = input(
        "{} say name of your first pokemon: ".format(first_user.title())).lower()

    while True:
        popped_pokemons = []
        if first_pokemon in pokemons_list:
            popped_pokemons.append(first_pokemon)
            pokemons_list.remove(first_pokemon)
            second_pokemon = input(
                "{} say name of your pokemon (name need to begin with"
                " the last letter of previous word): ".format(second_user.title())).lower()
            if second_pokemon[0] == first_pokemon[-1] and second_pokemon in pokemons_list:
                popped_pokemons.append(second_pokemon)
                pokemons_list.remove(first_pokemon)
                continue
            else:
                print("{} lose!" .format(second_user).title())
        else:
            print("{} lose!".format(first_user).title())


if __name__ == "__main__":
    main()
